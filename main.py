from graph import Graph
from search import BFSIterator, DFSIterator
from graph_algorithmA4 import*
from search_algorithms import*
from EulerianA5 import*
from A6 import VertexCoverApproximator

def graph_console():
    directed_input = input("Is the graph directed? (yes/no): ").strip().lower()
    weighted_input = input("Is the graph weighted? (yes/no): ").strip().lower()

    directed = directed_input == 'yes'
    weighted = weighted_input == 'yes'

    graph = Graph(directed=directed, weighted=weighted)
    graph_algorithms = GraphAlgorithms(graph)
    eulerian_algorihms = EulerianAlgorithms(graph)

    while True:
        print("\nGraph Console")
        print("1. Add vertex")
        print("2. Add edge")
        print("3. Remove edge")
        print("4. Remove vertex")
        print("5. Display graph")
        print("6. Get number of vertices")
        print("7. Get number of edges")
        print("8. Check if edge exists")
        print("9. Get outbound neighbors")
        print("10. Get inbound neighbors")
        print("11. Get all vertices")
        print("12. Set weight for an edge")
        print("13. Load graph from file")
        print("14. Perform BFS Traversal")
        print("15. Perform DFS Traversal")
        print("16. Run BEFS and A* search")
        print("17. Load coordonates from  file")
        print ("18.  Change if graph is directed ")
        print("19. Change if graph is weighted")
        print("20 Perform Topological Sort")
        print("21. Check if Graph is a DAG")
        print("22. Count Distinct Paths Between Two Vertices")
        print("23. Build a tree using preorder and inorder traversal ")
        print("24. Check if the Graph is Eulerian ")
        print("25. Find an Eulerian circuit using the Hierholzer algortihm ")
        print("26. Calculate Vertex Cover ")
        print("27. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                vertex = input("Enter vertex name: ")
                graph.add_vertex(vertex)
                print(f"Vertex {vertex} added.")

            elif choice == '2':
                u = input("Enter start vertex: ")
                v = input("Enter end vertex: ")
                weight = 1
                if graph._Graph__weighted:
                    weight = int(input("Enter weight: "))
                graph.add_edge(u, v, weight)
                print(f"Edge {u} -> {v} added.")

            elif choice == '3':
                u = input("Enter start vertex: ")
                v = input("Enter end vertex: ")
                graph.remove_edge(u, v)
                print(f"Edge {u} -> {v} removed.")

            elif choice == '4':
                vertex = input("Enter vertex name: ")
                graph.remove_vertex(vertex)
                print(f"Vertex {vertex} removed.")

            elif choice == '5':
                print("\nGraph Representation:")
                print(graph)

            elif choice == '6':
                print(f"Number of vertices: {graph.get_v()}")

            elif choice == '7':
                print(f"Number of edges: {graph.get_e()}")

            elif choice == '8':
                u = input("Enter start vertex: ")
                v = input("Enter end vertex: ")
                print(f"Edge {u} -> {v} exists: {graph.is_edge(u, v)}")

            elif choice == '9':
                vertex = input("Enter vertex name: ")
                print(f"Outbound neighbors of {vertex}: {graph.neighbors(vertex)}")

            elif choice == '10':
                vertex = input("Enter vertex name: ")
                print(f"Inbound neighbors of {vertex}: {graph.inbound_neighbors(vertex)}")

            elif choice == '11':
                print(f"Vertices: {graph.get_vertices()}")

            elif choice == '12':
                if not graph._Graph__weighted:
                    print("Graph is unweighted.")
                else:
                    u = input("Enter start vertex: ")
                    v = input("Enter end vertex: ")
                    w = int(input("Enter new weight: "))
                    graph.set_weight(u, v, w)
                    print(f"Weight for edge {u} -> {v} updated to {w}.")

            elif choice == '13':
                filename = input("Enter filename to load graph: ")
                graph.create_from_file(filename)
                print("Graph loaded successfully!")

            elif choice == '14':
                start_vertex = input("Enter start vertex for BFS: ")
                bfs_iterator = BFSIterator(graph, start_vertex)
                print("BFS Traversal Order (vertex, shortest path length):")
                for vertex, distance in bfs_iterator:
                    print(f"{vertex}: {distance}")

                target_vertex = input("Enter a vertex to check shortest path length (or press enter to skip): ")
                if target_vertex:
                    path_length = bfs_iterator.get_path_length(target_vertex)
                    if path_length is not None:
                        print(f"Shortest path length from {start_vertex} to {target_vertex}: {path_length}")
                    else:
                        print(f"No path from {start_vertex} to {target_vertex}.")

            elif choice == '15':
                start_vertex = input("Enter start vertex for DFS: ")
                try:
                    dfs_iterator = DFSIterator(graph, start_vertex)
                    print("DFS Traversal Order (vertex, discovery depth):")
                    for vertex, depth in dfs_iterator:
                        print(f"{vertex}: {depth}")
                except Exception as e:
                    print(f"Error during DFS: {e}")

            elif choice == '16':
                start = input("Enter start vertex: ")
                goal = input("Enter goal vertex: ")
                start = str(start)
                goal = str(goal)

                try:
                    graph.test_algorithms(start, goal)
                except Exception as e:
                    print(f"An error occurred while running algorithms: {e}")

            elif choice == '17':
                filename = input("Enter filename to load graph: ")
                graph.read_coordonates_file(filename)
                print("Graph loaded successfully!")

            elif choice == '18':
                current = 'directed' if graph._Graph__directed else 'undirected'
                print(f"Graph is currently {current}.")
                new_directed_input = input("Should the graph be directed? (yes/no): ").strip().lower()
                new_directed = new_directed_input == 'yes'
                graph.change_if_directed(new_directed)
                print("Graph direction updated.")

            elif choice == '19':
                current = 'weighted' if graph._Graph__weighted else 'unweighted'
                print(f"Graph is currently {current}.")
                new_weighted_input = input("Should the graph be weighted? (yes/no): ").strip().lower()
                new_weighted = new_weighted_input == 'yes'
                graph.change_if_weighted(new_weighted)
                print("Graph weighting updated.")

            elif choice == '20':
                sorted_vertices = graph_algorithms.topological_sort()
                print("Topological Sort Order:")
                print(sorted_vertices)

            elif choice == '21':
                if graph_algorithms.is_DAG():
                    print("The graph is a DAG (Directed Acyclic Graph).")
                else:
                    print("The graph is NOT a DAG (it has cycles).")

            elif choice == '22':
                source = input("Enter source vertex: ")
                destination = input("Enter destination vertex: ")
                if graph_algorithms.is_DAG():
                    num_paths = graph_algorithms.number_distinct_paths(source, destination)
                    print(f"Number of distinct paths from {source} to {destination}: {num_paths}")
                else:
                    print("Graph is not a DAG. Counting distinct paths is not supported for graphs with cycles.")

            elif choice == '23':
                preorder = input("Enter preorder traversal (comma separated): ").split(',')
                inorder = input("Enter inorder traversal (comma separated): ").split(',')

                preorder = [node.strip() for node in preorder]
                inorder = [node.strip() for node in inorder]

                graph_algorithms2 = TreeBuilder(preorder, inorder)

                try:
                    graph_algorithms2.build()
                    new_graph = graph_algorithms2.get_graph()
                    print("Tree built successfully! Here's the graph:")
                    print(new_graph)
                except Exception as e:
                    print(f"An error occurred while building the tree: {e}")

            elif choice == '24':
                try:
                    if eulerian_algorihms.isEulerian():
                        print("The graph is Eulerian.")
                    else:
                        print("The graph is not Eulerian.")
                except Exception as e:
                    print(f"An error occurred while checking Eulerian property: {e}")

            elif choice == '25':
                try:
                    if eulerian_algorihms.isEulerian():
                        circuit = eulerian_algorihms.HierholzerAlgorithm()
                        print("Eulerian circuit found:")
                        print(" -> ".join(circuit))
                    else:
                        print("The graph is not Eulerian. No Eulerian circuit exists.")
                except Exception as e:
                    print(f"An error occurred while finding Eulerian circuit: {e}")

            elif choice == '26':
                try:
                    approximator = VertexCoverApproximator(graph)
                    cover = approximator.approximate_vertex_cover()
                    print("Approximated Vertex Cover (Greedy):")
                    print(cover)
                except Exception as e:
                    print(f"An error occurred while computing vertex cover: {e}")

            elif choice == '27':
                print("Exiting...")
                break

            else:
                print("Invalid choice, please try again.")

        except Exception as e:
            print(f"An error occurred: {e}. Continuing...")

if __name__ == '__main__':
    graph_console()
