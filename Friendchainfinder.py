import streamlit as st
from collections import defaultdict, deque
import networkx as nx
import matplotlib.pyplot as plt

# --- Existing functions and logic ---
def initialize_union_find(n):
    """Initialize the parent and rank arrays for Union-Find."""
    parent = list(range(n))
    rank = [0] * n
    return parent, rank

def find(parent, x):
    """Find the representative (root) of the set containing x with path compression."""
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # Path compression
    return parent[x]

def union(parent, rank, x, y):
    """Union two sets containing x and y by rank."""
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

def build_graph(friendships):
    """Create an adjacency list from the friendships."""
    graph = defaultdict(list)
    for friend1, friend2 in friendships:
        graph[friend1].append(friend2)
        graph[friend2].append(friend1)
    return graph

def bfs_shortest_path(graph, start, end):
    """Find the shortest path using BFS."""
    queue = deque([(start, [start])])  # Queue stores (current_person, path_so_far)
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current == end:
            return path  # Return the shortest path when destination is reached

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return []  # Return empty list if no path exists

def shortest_friend_chain(people, friendships, start, end):
    # Step 1: Map people's names to numeric indices
    name_to_index = {name: i for i, name in enumerate(people)}
    index_to_name = {i: name for name, i in name_to_index.items()}

    # Step 2: Initialize Union-Find structures
    n = len(people)
    parent, rank = initialize_union_find(n)

    # Step 3: Perform Union-Find to group connected components
    for friend1, friend2 in friendships:
        union(parent, rank, name_to_index[friend1], name_to_index[friend2])

    # Step 4: Check if start and end are in the same component
    if find(parent, name_to_index[start]) != find(parent, name_to_index[end]):
        return []  # No path exists between start and end

    # Step 5: Build the adjacency list (graph)
    mapped_friendships = [(name_to_index[friend1], name_to_index[friend2]) for friend1, friend2 in friendships]
    graph = build_graph([(index_to_name[a], index_to_name[b]) for a, b in mapped_friendships])

    # Step 6: Use BFS to find the shortest path between start and end
    shortest_path = bfs_shortest_path(graph, start, end)
    return shortest_path

# --- New Visualization Function ---
def visualize_friend_network(graph, shortest_path):
    """Visualize the friend network and highlight the shortest path."""
    G = nx.Graph()

    # Add edges to the graph
    for person, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(person, neighbor)

    # Highlight the shortest path in the graph
    edge_colors = ["red" if (a, b) in zip(shortest_path, shortest_path[1:]) or (b, a) in zip(shortest_path, shortest_path[1:]) else "black" for a, b in G.edges]

    # Adjust the layout to bring nodes closer
    pos = nx.spring_layout(G, k=0.5, seed=42)  # Decrease k to make nodes closer

    # Plot the graph
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color=edge_colors, node_size=1500, font_size=10)
    plt.title("Friend Network")
    st.pyplot(plt)  # Display the graph in Streamlit

# --- Streamlit UI ---
def main():
    st.title("Friend Chain Finder")

    # People list and friendships
    people = [
    "Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Hannah",
    "Ivy", "Jack", "Karen", "Leo", "Mona", "Nathan", "Olivia", "Paul", 
    "Quinn", "Rachel", "Sam", "Tina", "Uma", "Victor", "Wendy", "Xander",
    "Yara", "Zane"]

    friendships = [
    ("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "David"), ("Charlie", "Emma"),
    ("David", "Frank"), ("Emma", "Grace"), ("Frank", "Hannah"), ("Grace", "Ivy"),
    ("Ivy", "Jack"), ("Jack", "Karen"), ("Karen", "Leo"),  # Leo is isolated here
    ("Mona", "Nathan"), ("Nathan", "Olivia"), ("Olivia", "Paul"),
    ("Paul", "Quinn"), ("Quinn", "Rachel"),  # Rachel is isolated here
    ("Alice", "Grace"), ("David", "Ivy"), ("Frank", "Karen"),
]

    # Input fields for start and end
    start = st.text_input("Enter the start person:")
    end = st.text_input("Enter the end person:")

    if st.button("Find Friend Chain"):
        if start and end:
            if start not in people or end not in people:
                st.error("Both start and end people must be in the list.")
            else:
                chain = shortest_friend_chain(people, friendships, start, end)
                if chain:
                    st.success(f"Shortest chain from {start} to {end}: {' -> '.join(chain)}")

                    # Build the adjacency list (graph) and visualize it
                    graph = build_graph(friendships)
                    visualize_friend_network(graph, chain)
                else:
                    st.error(f"No chain exists between {start} and {end}.")
        else:
            st.warning("Please enter both start and end people.")

if __name__ == "__main__":
    main()
