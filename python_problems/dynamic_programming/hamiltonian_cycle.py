
class Graph():

    def __init__(self, vertices):
        """
        Initializing vertices
        """
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
        self.V = vertices


    """
    Check if the vertex is an adjacent vertex of the previously added vertex
    and is not included in the path earlier
    """
    def isSafe(self, v, pos, path):

        """
        Check if the current vertex and the last vertex
        if the path are adjacent
        """
        if self.graph[path[po s -1]][v] == 0:
            return False


        # Check if the current vertex not already in the path
        for vertex in path:
            if vertex == v:
                return False

        return True

    def hamCycle(self):
        '''
        Initialize
        '''


    def hamCycleUtil(self, path, pos):
        # Base Case: If all vertices are included in the path
        if pos == self.V:
            # Last vertex must be adjacent to the first vertex in the cycle
            if self.graph[path[pos -1]][path[0]] == 1:
                return True
            else:
                return False


        for v in range(1, self.V):

            if self.isSafe(v, pos, path) == True:
                path[pos] = v
