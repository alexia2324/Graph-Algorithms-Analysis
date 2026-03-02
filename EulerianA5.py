from graph import*
class EulerianAlgorithms:
    def __init__(self,Graph):
        self.__graph=Graph

    def isEulerian(self):
        #complexity:O(v)
        if self.__graph.is_directed():
            for v in self.__graph.get_vertices():
                if len(self.__graph.inbound_neighbors(v)) != len(self.__graph.neighbors(v)):
                    return False
        else:
            for v in self.__graph.get_vertices():
                if len(self.__graph.neighbors(v)) % 2 != 0:
                    return False
        return True

    def HierholzerAlgorithm(self):
        # Complexity O(V+E)
        if not self.isEulerian():
            return []

        stack = deque()
        circuit = []
        neighbors = {}

        for v in self.__graph.get_vertices():#O(V)
            neighbors[v] = set(self.__graph.neighbors(v))#O(V)

        start = self.__graph.get_vertices()[0]
        stack.append(start)

        while stack:
            current = stack[-1]
            if neighbors[current]:
                next_node = neighbors[current].pop()
                if not self.__graph.is_directed():
                    neighbors[next_node].remove(current)
                stack.append(next_node)
            else:
                circuit.append(stack.pop())

        return circuit[::-1]








