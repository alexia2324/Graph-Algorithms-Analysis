
from graph import*
# Create a graph
g = Graph()

# Add vertices
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

# Add edges
g.add_edge("A", "B")
g.add_edge("B", "C")
g.add_edge("C", "D")
g.add_edge("D", "A")

# Print graph
print(g)  # Should match CS Academy format

# Check edges
print(g.is_edge("A", "B"))  # True
print(g.is_edge("B", "A"))  # False

# Get neighbors
print(g.neighbors("B"))  # ["C"]
print(g.inbound_neighbors("C"))  # ["B"]

# Get total vertices and edges
print(g.get_v())  # 4
print(g.get_e())  # 4

# Remove edge and vertex
g.remove_edge("A", "B")
g.remove_vertex("D")

print(g)  # Updated graph

"""    def __str__(self):
        line1=[]
        line1.append("directed" if self.__directed else "undirected")
        line1.append("weighted" if self.__weighted else "unweighted")
        result = [" ".join(line1)]
        vertices = list(self.__adj_list.keys())

        # Add edges
        for i, u in enumerate(vertices):
            for j, v in enumerate(vertices):
                if self.__adj_list[u][j] == 1:
                    if not self.__directed and i > j:
                        continue
                    result.append(f"{u} {v}")

        # Add isolated vertices (vertices with no edges)
        for v in vertices:
            if all(value == 0 for value in self.__adj_list[v]):  # No outbound edges
                if not any(self.__adj_list[u][vertices.index(v)] for u in vertices):  # No inbound edges
                    result.append(v)

        return "\n".join(result)"""


from graph import Graph
from search_algorithms import GreedyBestFirstSearch, AStarSearch, euclidean_heuristic
g = Graph(directed=False, weighted=True)
g.create_from_file("graf.txt")
g.read_coordonates_file("coordonate.txt")

start = "A"
goal = "F"

gbfs = GreedyBestFirstSearch(g, start, goal, euclidean_heuristic)
astar = AStarSearch(g, start, goal, euclidean_heuristic)

print("Greedy BFS path:", gbfs.run())
print("A* path:", astar.run())



import time

def test_algorithms(graph_file, start, goal):
    g = Graph()
    g.create_from_file(graph_file)

    print(f"\n=== Testing on graph: {graph_file} ===")
    print(f"Start: {start}, Goal: {goal}")

    # Greedy Best First Search
    print("\n--- Greedy Best First Search ---")
    Metrics.reset()
    start_time = time.perf_counter()
    greedy = GreedyBestFirstSearch(g)
    path = greedy.search(start, goal)
    end_time = time.perf_counter()

    cost = 0
    for i in range(len(path) - 1):
        cost += g.get_weight(path[i], path[i + 1])

    print(f"Path: {path}")
    print(f"Cost: {cost}")
    print(f"Edge checks: {Metrics.edge_checks}")
    print(f"Priority queue operations: {Metrics.priority_ops}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")

    # A* Search
    print("\n--- A* Search ---")
    Metrics.reset()
    start_time = time.perf_counter()
    astar = AStarSearch(g)
    path = astar.search(start, goal)
    end_time = time.perf_counter()

    cost = 0
    for i in range(len(path) - 1):
        cost += g.get_weight(path[i], path[i + 1])

    print(f"Path: {path}")
    print(f"Cost: {cost}")
    print(f"Edge checks: {Metrics.edge_checks}")
    print(f"Priority queue operations: {Metrics.priority_ops}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")

""""""