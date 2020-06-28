class GraphByMatrix:
    def __init__(self, vertices, matrix):
        self.vertices = vertices
        self.size = len(vertices)
        self.matrix = matrix

    def printMatrx(self):
        for row in range(self.size):
            for column in range(self.size):
                print("%d" % self.matrix[row][column], end=' ')
            print()
        #print(self.matrix)

    def setEdge(self, v1, v2, value):
        v1Index = self.vertices.index(v1)
        v2Index = self.vertices.index(v2)
        self.matrix[v1Index][v2Index] = value

    def dfs(self, vertice):
        visited = [0] * self.size
        v = self.vertices.index(vertice) 
        self.__dfs(v, visited)
        print()

    def __dfs(self, v, visited):
        visited[v] = 1
        print(self.vertices[v], end=' ')
        for u in range(self.size):
            if self.matrix[v][u] == 1 and visited[u] == 0:
                self.__dfs(u, visited)

    def bfs(self, vertice):
        queue = []
        v = self.vertices.index(vertice)
        self.__bfs(v, queue)
        print()

    def __bfs(self, v, queue):
        visited = [0] * self.size
        queue.append(v)
        while len(queue) != 0:
            print(self.vertices[v], end=' ')
            for u in range(self.size):
                if self.matrix[v][u] == 1 and visited[u] == 0:
                    queue.append(u)


def main():
    matrix = [[0,0],[1,0]]
    graph = GraphByMatrix([1,2], matrix)
    graph.printMatrx()
    graph.setEdge(1, 2, 1)
    graph.dfs(1)

if __name__ == "__main__":
    main()

