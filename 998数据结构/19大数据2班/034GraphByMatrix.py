class Graph:
    def __init__(self, vertices, matrix):
        self.vertices = vertices    #结点的列表
        self.matrix = matrix        #邻接矩阵
        self.vCount = len(vertices) #节点的个数
    
    def dfs(self, vertice):
        vIndex = self.vertices.index(vertice) #得到vertice的索引
        visited = [0] * self.vCount
        self.__dfs(vIndex, visited)
        print()

    def __dfs(self, v, visited):
        visited[v] = 1      #记录v节点已经被访问过了
        #通过打印节点说明遍历到该节点
        print("(%d)" % self.vertices[v], end=' ')
        for u in range(self.vCount):
            if self.matrix[v][u] == 1 and visited[u] == 0:
                self.__dfs(u, visited) #递归地在u上深搜

    def ydfs(self, vertice):
        v = self.vertices.index(vertice) #得到vertice的索引
        self.__ydfs(v)
        print()

    def __ydfs(self, v):
        print(self.vertices[v], end=' ')
        for u in range(self.vCount):
            if self.matrix[v][u] == 1: #可用的边
                self.matrix[v][u] = 0
                self.matrix[u][v] = 0
                self.__ydfs(u)

    def bfs(self, vertice):
        v = self.vertices.index(vertice) #得到vertice的索引
        queue = []
        queue.append(v)   #入队第1个节点
        visited = [0] * self.vCount
        visited[v] = 1
        while len(queue) != 0 : #当队列非空时继续
            v = queue.pop(0) #出队
            print("(%d) " % self.vertices[v], end='')
            for u in range(self.vCount):
                if self.matrix[v][u] == 1 and visited[u] == 0:
                    visited[u] = 1 #标记u已经入队
                    queue.append(u)
        print()

graph = Graph([1,2,3,4,5], [[0,1,1,0,0],[1,0,0,1,1],[1,0,0,1,0],[0,1,1,0,1],[0,1,0,1,0]])
#graph = Graph([1,2,3,4], [[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]])
graph.dfs(1)
#graph.ydfs(1)
graph.bfs(1)




