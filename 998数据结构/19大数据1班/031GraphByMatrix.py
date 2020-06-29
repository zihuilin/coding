class Graph:
    def __init__(self, vertices, matrix):
        self.vertices = vertices    #节点list
        self.matrix = matrix        #邻接矩阵
        self.vcount = len(vertices) #节点的个数

    def dfs(self, vertice):
        vIndex = self.vertices.index(vertice)
        visited = [0] * self.vcount
        self.__dfs(vIndex, visited)
        print()
    
    def __dfs(self, v, visited):
        #在visited列表中记录已经访问了v节点
        visited[v] = 1
        print("(%d)" % self.vertices[v], end=' ')  #通过打印说明遍历到v节点
        for u in range(self.vcount):
            if self.matrix[v][u] == 1 and visited[u] == 0:
                self.__dfs(u, visited) #递归访问u节点

graph = Graph([1, 2, 3, 4, 5], [[0,1,1,0,0],[1,0,0,1,1],[1,0,0,1,0],[0,1,1,0,1],[0,1,0,1,0]])
graph.dfs(1)

