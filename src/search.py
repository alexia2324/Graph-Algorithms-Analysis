from collections import deque

class BFSIterator:
    def __init__(self, graph, start_vertex):
        self.__graph = graph
        self.__queue = deque()
        self.__visited = set()
        self.__distances = {}

        if start_vertex not in self.__graph.get_vertices():
            raise ValueError(f"{start_vertex} is not a valid vertex.")

        self.__queue.append(start_vertex)
        self.__visited.add(start_vertex)
        self.__distances[start_vertex] = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.__queue:
            raise StopIteration

        current = self.__queue.popleft()
        for neighbor in self.__graph.neighbors(current):
            if neighbor not in self.__visited:
                self.__visited.add(neighbor)
                self.__queue.append(neighbor)
                self.__distances[neighbor] = self.__distances[current] + 1

        return current, self.__distances[current]

    def get_path_length(self, vertex):
        return self.__distances.get(vertex)

class DFSIterator:
    def __init__(self, graph, start_vertex):
        self.__graph = graph
        self.__stack = []
        self.__visited = set()
        self.__distances = {}

        if start_vertex not in self.__graph.get_vertices():
            raise ValueError(f"{start_vertex} is not a valid vertex.")

        self.__stack.append((start_vertex, 0))

    def __iter__(self):
        return self

    def __next__(self):
        while self.__stack:
            current, depth = self.__stack.pop()
            if current not in self.__visited:
                self.__visited.add(current)
                self.__distances[current] = depth

                # Reversed so the leftmost neighbor is visited first
                for neighbor in reversed(self.__graph.neighbors(current)):
                    if neighbor not in self.__visited:
                        self.__stack.append((neighbor, depth + 1))

                return current, depth

        raise StopIteration

    def get_path_length(self, vertex):
        return self.__distances.get(vertex)
