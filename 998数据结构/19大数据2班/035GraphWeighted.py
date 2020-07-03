class Graph:
    def __init__(self, vertices, matrix):
        self.vertices = vertices    #节点list
        self.matrix = matrix        #邻接矩阵
        self.vcount = len(vertices) #节点的个数

    def printMatrix(self):
        for u in range(self.vcount):
            for v in range(self.vcount):
                print(str(self.matrix[u][v]), end=' ')
            print()
        
    def floyed(self):
        m = [[0 for u in range(self.vcount)] for v in range(self.vcount)]
        for u in range(self.vcount):
            for v in range(self.vcount):
                m[u][v] = self.matrix[u][v]
        for k in range(self.vcount):
            for u in range(self.vcount):
                for v in range(self.vcount):
                    if m[u][v] > m[u][k] + m[k][v]:
                        m[u][v] = m[u][k] + m[k][v]
        return m

m = [[float('inf') for u in range(5)] for v in range(5)]

m[0][1] = m[1][0] = 2
m[0][2] = m[2][0] = 4
m[0][3] = m[3][0] = 7
m[1][2] = m[2][1] = 1
m[2][3] = m[3][2] = 1
m[1][4] = m[4][1] = 2
m[2][4] = m[4][2] = 6

graph = Graph([1, 2, 3, 4, 5], m)
rm = graph.floyed()
print(rm[0][3])

