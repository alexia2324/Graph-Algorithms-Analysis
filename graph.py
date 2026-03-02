from collections import deque
from search import *
from search_algorithms import *
from search_algorithms import GreedyBestFirstSearch


class Graph:
    def __init__(self, directed=True, weighted=False):
        self.__directed = directed
        self.__weighted = weighted
        self.__matrix = {}
        self.__vertex_list = []
        self._coordonates = {}

    def is_directed(self):
        return self.__directed

    def add_vertex(self, vertex):
        # O(V)
        if vertex in self.__matrix:
            raise ValueError(f"Vertex {vertex} already exists.")
        self.__vertex_list.append(vertex)
        for row in self.__matrix.values():
            row.append(None)
        self.__matrix[vertex] = [None] * len(self.__vertex_list)

    def add_edge(self, u, v, weight=None):
        # O(V)
        if u not in self.__matrix or v not in self.__matrix:
            raise ValueError("Both vertices must exist.")

        if u == v:
            raise ValueError("No self-loops allowed.")

        if not self.__weighted:
            weight = 1
        elif weight is None:
            raise ValueError("Weighted graph requires a weight.")

        u_index = self.__vertex_list.index(u)
        v_index = self.__vertex_list.index(v)

        if self.__matrix[u][v_index] is not None:
            raise ValueError("Edge already exists.")
        if not self.__directed and self.__matrix[v][u_index] is not None:
            raise ValueError("Edge already exists (undirected).")
        self.__matrix[u][v_index] = weight
        if not self.__directed:
            self.__matrix[v][u_index] = weight

    def remove_edge(self, u, v):
        # O(V)
        if u not in self.__matrix or v not in self.__matrix:
            raise ValueError("Invalid vertex.")
        v_index = self.__vertex_list.index(v)
        if self.__matrix[u][v_index] is None:
            raise ValueError("Edge does not exist.")
        self.__matrix[u][v_index] = None
        if not self.__directed:
            u_index = self.__vertex_list.index(u)
            self.__matrix[v][u_index] = None

    def remove_vertex(self, vertex):
        # O(V^2)
        if vertex not in self.__matrix:
            raise ValueError("Vertex does not exist.")
        index = self.__vertex_list.index(vertex)
        self.__vertex_list.remove(vertex)
        self.__matrix.pop(vertex)
        for row in self.__matrix.values():
            row.pop(index)

    def get_v(self):
        # O(1)
        return len(self.__matrix)

    def get_e(self):
        # O(V^2)
        count = sum(1 for row in self.__matrix.values() for val in row if val is not None)
        return count if self.__directed else count // 2

    def is_edge(self, u, v):
        # O(V)
        if u not in self.__matrix or v not in self.__matrix:
            raise ValueError("Invalid vertex.")
        v_index = self.__vertex_list.index(v)
        return self.__matrix[u][v_index] is not None

    def neighbors(self, vertex):
        # O(V)
        if vertex not in self.__matrix:
            raise ValueError("Vertex not in graph.")
        neighbors = []
        row = self.__matrix[vertex]
        for i in range(len(row)):
            if row[i] is not None:
                neighbor = self.__vertex_list[i]
                neighbors.append(neighbor)
        return neighbors

    def inbound_neighbors(self, vertex):
        # O(V)
        if vertex not in self.__matrix:
            raise ValueError("Vertex not in graph.")
        index = self.__vertex_list.index(vertex)
        incoming_vertices = []
        for v in self.__matrix:
            row = self.__matrix[v]
            if row[index] is not None:
                incoming_vertices.append(v)
        return incoming_vertices

    def get_vertices(self):
        # O(V)
        return list(self.__vertex_list)

    def change_if_directed(self, new_directed):
        # O(V^2)
        if self.__directed == new_directed:
            return
        if not new_directed:
            # Make symmetric
            for u in self.__vertex_list:
                for i, weight in enumerate(self.__matrix[u]):
                    if weight is not None:
                        v = self.__vertex_list[i]
                        v_index = self.__vertex_list.index(u)
                        self.__matrix[v][v_index] = weight
        self.__directed = new_directed

    def change_if_weighted(self, new_weighted):
        # O(V^2)
        if self.__weighted == new_weighted:
            return
        for u in self.__matrix:
            for i in range(len(self.__matrix[u])):
                if self.__matrix[u][i] is not None:
                    self.__matrix[u][i] = 0 if new_weighted else 1
        self.__weighted = new_weighted

    def get_weight(self, u, v):
        # O(V)
        if not self.__weighted:
            raise ValueError("Graph is not weighted.")
        v_index = self.__vertex_list.index(v)
        if self.__matrix[u][v_index] is None:
            raise ValueError("Edge does not exist.")
        return self.__matrix[u][v_index]

    def set_weight(self, u, v, weight):
        # O(V)
        if not self.__weighted:
            raise ValueError("Graph is not weighted.")
        v_index = self.__vertex_list.index(v)
        if self.__matrix[u][v_index] is None:
            raise ValueError("Edge does not exist.")
        self.__matrix[u][v_index] = weight
        if not self.__directed:
            u_index = self.__vertex_list.index(u)
            self.__matrix[v][u_index] = weight

    def __str__(self):
        # O(V^2)
        lines = [f"{'directed' if self.__directed else 'undirected'} {'weighted' if self.__weighted else 'unweighted'}"]
        for i, u in enumerate(self.__vertex_list):
            has_edge = False
            for j, weight in enumerate(self.__matrix[u]):
                if weight is not None:
                    if self.__directed or i <= j:  # avoid duplicates for undirected
                        v = self.__vertex_list[j]
                        if self.__weighted:
                            lines.append(f"{u} {v} {weight}")
                        else:
                            lines.append(f"{u} {v}")
                    has_edge = True
            if not has_edge:
                lines.append(f"{u}")
        return "\n".join(lines)

    def create_from_file(self, filename):
        # O(V^2)
        with open(filename, 'r') as f:
            lines = f.read().splitlines()

        type_line = lines[0].strip().split()
        self.__directed = 'directed' in type_line
        self.__weighted = 'weighted' in type_line

        self.__matrix = {}
        self.__vertex_list = []

        vertices = set()
        edges = []

        for line in lines[1:]:
            parts = line.strip().split()
            if len(parts) == 1:
                vertices.add(parts[0])
            elif len(parts) == 2:
                vertices.update(parts[:2])
                edges.append((parts[0], parts[1], None))
            elif len(parts) == 3:
                vertices.update(parts[:2])
                edges.append((parts[0], parts[1], int(parts[2])))

        for v in vertices:
            self.add_vertex(v)

        for u, v, w in edges:
            self.add_edge(u, v, w)

    def read_coordonates_file(self, filename):
        with open(filename, 'r') as f:
            lines = f.read().splitlines()
        for line in lines[1:]:
            parts = line.strip().split(',')
            name, x, y = parts
            self._coordonates[name] = (float(x), float(y))
        print("Coordonate încărcate:", self._coordonates)

    def BFS_iter(self, start_vertex):
        return self.BFSIterator(self, start_vertex)

    def DFS_iter(self, start_vertex):
        return self.DFSIterator(self, start_vertex)

    def test_algorithms(self, start, goal):

        print(f"\nMinimum cost walk {start} to {goal}:")

        Metrics.reset()
        greedy = GreedyBestFirstSearch(self)
        t0 = time.time()
        path_greedy = greedy.search(start, goal)
        t1 = time.time()
        greedy_time = int((t1 - t0) * 1000)
        greedy_pushes = Metrics.priority_ops
        greedy_pops = greedy_pushes  # assumed equal

        print(f"Greedy Best First Search: time: {greedy_time}ms, cost: -, path: {', '.join(path_greedy)}")

        # === A* SEARCH ===
        Metrics.reset()
        astar = AStarSearch(self)
        t0 = time.time()
        path_astar, cost_astar = astar.search(start, goal)
        t1 = time.time()
        astar_time = int((t1 - t0) * 1000)
        astar_pushes = Metrics.priority_ops
        astar_pops = astar_pushes

        print(f"A*: time: {astar_time}ms, cost: {cost_astar}, path: {', '.join(path_astar)}")

        # === COMPARISON ===
        print("\nComparison:")
        print(f"{'':<16} {'g.cost':<8} {'pq.push':<9} {'pq.pop'}")
        print(f"{'Greedy BFS':<16} {'-':<8} {greedy_pushes:<9} {greedy_pops}")
        print(f"{'A*':<16} {cost_astar:<8} {astar_pushes:<9} {astar_pops}")
