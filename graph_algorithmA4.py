from graph import*
from collections import deque

class GraphAlgorithms:
    def __init__(self,Graph):
        self.__graph=Graph

    def topological_sort(self):
        #Complexity O(V^2)
        sorted_list = []
        q = deque()
        count = {}
        for v in self.__graph.get_vertices(): # O(V)
            count[v] = len(self.__graph.inbound_neighbors(v))# O(V)
            if count[v] == 0:
                q.append(v)
        while q:
            current = q.popleft()
            sorted_list.append(current)
            for neighbor in self.__graph.neighbors(current):
                count[neighbor] -= 1
                if count[neighbor] == 0:
                    q.append(neighbor)
        return sorted_list

    def is_DAG(self):
        return len(self.topological_sort()) == self.__graph.get_v()

    def number_distinct_paths(self, start, end):
        #Complexity(m+n)
        if not self.is_DAG():
            return None
        topo_order = GraphAlgorithms.topological_sort(self)
        paths = {v: 0 for v in self.__graph.get_vertices()}
        paths[start] = 1

        for u in topo_order:
            for v in self.__graph.neighbors(u):
                paths[v] = paths[v]+paths[u]
        return paths[end]



class TreeBuilder:
    def __init__(self, preorder, inorder):
        #O(n^2)
        self.__preorder = deque(preorder)
        self.__inorder = inorder
        self.__graph = Graph(directed=True, weighted=False)

    def build(self):
        return self._build_subtree(self.__inorder)

    def _build_subtree(self, inorder_sublist):
        if not inorder_sublist:
            return None

        root_value = self.__preorder.popleft()
        if root_value not in self.__graph.get_vertices():
            self.__graph.add_vertex(root_value)

        root_index = inorder_sublist.index(root_value)

        left_subtree = self._build_subtree(inorder_sublist[:root_index])
        right_subtree = self._build_subtree(inorder_sublist[root_index + 1:])

        if left_subtree:
            self.__graph.add_edge(root_value, left_subtree)
        if right_subtree:
            self.__graph.add_edge(root_value, right_subtree)

        return root_value

    def get_graph(self):
        return self.__graph
