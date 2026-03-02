from graph import Graph
class VertexCoverApproximator:
    def __init__(self, graph: Graph):
        #Complexity:O(V ^ 3)
        if graph.is_directed():#O(1)
            raise ValueError("Vertex cover approximation requires an undirected graph.")
        self.__graph = graph

    def approximate_vertex_cover(self):
        import copy
        graph_copy = copy.deepcopy(self.__graph)
        cover = set()

        while graph_copy.get_e() > 0: # O(1)
            max_deg = -1
            max_vertex = None

            for v in graph_copy.get_vertices():# O(V)
                deg = len(graph_copy.neighbors(v)) # O(V)
                if deg > max_deg:
                    max_deg = deg
                    max_vertex = v

            if max_vertex is None:
                break

            cover.add(max_vertex)

            for neighbor in graph_copy.neighbors(max_vertex): # O(V)
                graph_copy.remove_edge(max_vertex, neighbor)

        return cover
