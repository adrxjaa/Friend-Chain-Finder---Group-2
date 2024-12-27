# Friend-Chain-Finder---Group-2


# Friend Chain Finder

Friend Chain Finder is a mini-project created for our Fundamentals of AI course. It implements BFS and Union-Find algorithms to explore and visualize connections within a social network. This project also features a Streamlit web interface for user interaction.

## Features
- **Friendship Graph**: Represent friendships as an undirected graph.
- **Connection Finder**: Use BFS to find the shortest path between two individuals.
- **Group Detection**: Identify connected components using the Union-Find algorithm.
- **Interactive UI**: Simple and user-friendly interface built with Streamlit.
- **Visualization**: Highlights the shortest path in the friendship graph using NetworkX and Matplotlib.

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - `streamlit` for the web interface.
  - `networkx` for graph-related operations.
  - `matplotlib` for visualizing the graph.
  - `collections` for data structures like deque and defaultdict.

## Project Structure
```
FriendChainFinder/
├── src/
│   ├── app.py            # Main Streamlit application
│   ├── bfs.py            # BFS implementation
│   ├── union_find.py     # Union-Find implementation
│   ├── graph_utils.py    # Utility functions for graph operations
├── tests/
│   └── test_algorithms.py # Unit tests for BFS and Union-Find
├── README.md             # Project documentation
└── requirements.txt      # List of dependencies
```

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/FriendChainFinder.git
   ```
2. Navigate to the project directory:
   ```bash
   cd FriendChainFinder
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Streamlit application:
   ```bash
   streamlit run src/app.py
   ```
2. Use the web interface to:
   - Input the start and end people.
   - View the shortest friend chain and its visualization.


## Code Overview
### Algorithms
- **Union-Find**: Groups connected components efficiently.
- **BFS (Breadth-First Search)**: Finds the shortest path between two nodes.

### Visualization
- **NetworkX**: Constructs and manages the graph.
- **Matplotlib**: Plots the graph with highlighted paths.

### Streamlit UI
- Accepts user inputs for start and end nodes.
- Displays results interactively.
- Handles errors and edge cases gracefully.




