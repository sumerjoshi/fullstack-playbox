from collections import defaultdict


class Graph(object):

    # Dictionary of lists (containing adjacency list)
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices  # No of vertices

    def addEdge(self, u, v):
        """
        Using default dict to append value to key
        :param u:
        :param v:
        :return:
        """
        self.graph[u].append(v)

    def topSort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] is False:
                self.topSortUtil(i, visited, stack)

        return stack

    def topSortUtil(self, vertex, visited, stack):
        visited[vertex] = True

        for i in range(self.V):
            if visited[i] is False:
                self.topSortUtil(i, visited, stack)

        stack.insert(0, vertex)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print(g.topSort())
