from graph import*
import math
import heapq
import time

class Metrics:
    edge_checks = 0
    priority_ops = 0
    @staticmethod
    def reset():
        Metrics.edge_checks = 0
        Metrics.priority_ops = 0

class GreedyBestFirstSearch:
    def __init__(self, Graph):
        self.__graph = Graph

    def euclidean_heuristic(self, node1, node2):
        c1 = self.__graph._coordonates[node1]
        c2 = self.__graph._coordonates[node2]
        return math.sqrt(((c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2))

    def search(self, start, goal):
        # O(V log V )
        pq = []
        heapq.heappush(pq, (self.euclidean_heuristic(start, goal), start))
        Metrics.priority_ops += 1
        visited = set()
        previous = {start: None}

        while pq:
            _, current = heapq.heappop(pq)
            if current == goal:
                break
            if current in visited:
                continue

            visited.add(current)
            for neighbor in self.__graph.neighbors(current):
                Metrics.edge_checks += 1
                if neighbor not in visited:
                    previous[neighbor] = current
                    heapq.heappush(pq, (self.euclidean_heuristic(neighbor, goal), neighbor))
                    Metrics.priority_ops += 1

        return self.reconstruct_path(previous, start, goal)

    def reconstruct_path(self, previous, start, goal):
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = previous.get(node)
        path.reverse()
        return path

class AStarSearch:
    def __init__(self, Graph):
        self.__graph = Graph

    def euclidean_heuristic(self, node1, node2):
        c1 = self.__graph._coordonates[node1]
        c2 = self.__graph._coordonates[node2]
        return math.sqrt(((c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2))

    def search(self, start, goal):
        # O(V log V + V²)
        pq = []
        heapq.heappush(pq, (0 + self.euclidean_heuristic(start, goal), start))
        Metrics.priority_ops +=1
        distance = {v: float('inf') for v in self.__graph.get_vertices()}
        distance[start] = 0
        previous = {start: None}

        while pq:
            _, current = heapq.heappop(pq) # O(log V)
            Metrics.priority_ops += 1

            if current == goal:
                break

            for neighbor in self.__graph.neighbors(current):# O(V)
                Metrics.edge_checks += 1
                cost = self.__graph.get_weight(current, neighbor)#O(V)
                Metrics.edge_checks += 1
                new_cost = distance[current] + cost
                if new_cost < distance[neighbor]:
                    distance[neighbor] = new_cost
                    priority = new_cost + self.euclidean_heuristic(neighbor, goal)
                    heapq.heappush(pq, (priority, neighbor))# O(log V)
                    Metrics.priority_ops += 1
                    previous[neighbor] = current

        return self._reconstruct_path(previous, start, goal), distance[goal]

    def _reconstruct_path(self, previous, start, goal):
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = previous.get(node)
        path.reverse()
        return path

