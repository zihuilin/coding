class Graph:
    def __init__(self, vertices, matrix):
        self.vertices = vertices    #节点list
        self.matrix = matrix        #邻接矩阵
        self.vcount = len(vertices) #节点的个数

    def printMatrix(self):
        for u in range(self.vcount):
            for v in range(self.vcount):
                print(self.matrix[u][v], end=' ')
            print()
        print()

    def floyed(self):
        m = [[0] * 5 for v in range(5)]
        for u in range(self.vcount):
            for v in range(self.vcount):
                m[u][v] = self.matrix[u][v]
        #在克隆的matrix：m上做floyed算法
        for k in range(self.vcount):
            for s in range(self.vcount):
                for e in range(self.vcount):
                    if m[s][e] > m[s][k] + m[k][e]:
                        m[s][e] = m[s][k] + m[k][e]
        return m

    def dijkstra(self, s): #s为起始点的索引
        dis = [float('inf')] * self.vcount #所有点的最短距离为无穷大
        visited = [0] * self.vcount    #一开始所有点都没有确定最短距离
        count = 0 #已经确定最短距离的点的个数
        dis[s] = 0     #最原始的信息：开始点到自己的距离为0
        while count < self.vcount:
            minD = float('inf')
            minV = -1
            for u in range(self.vcount):
                if visited[u] == 0 and dis[u] < minD:
                    minD = dis[u] #距离的最小值
                    minV = u  #更新距离最小值的节点的索引
            for v in range(self.vcount): #更新那些经过minV距离更短的节点
                if dis[v] > dis[minV] + self.matrix[minV][v]:
                    dis[v] = dis[minV] + self.matrix[minV][v]
            visited[minV] = 1
            count = count + 1
        return dis

m = [[float('inf')] * 5 for v in range(5)]

m[0][1] = m[1][0] = 2  #结点1的索引为0, 结点2的索引为1
m[0][2] = m[2][0] = 4
m[0][3] = m[3][0] = 7
m[1][2] = m[2][1] = 1
m[2][3] = m[3][2] = 1
m[1][4] = m[4][1] = 2
m[2][4] = m[4][2] = 6

graph = Graph([1, 2, 3, 4, 5], m)
graph.printMatrix()
#rm = graph.floyed()
#print(rm[0][4]) #打印结点1到结点5的最短距离
dis = graph.dijkstra(0)  #从结点1开始，找到其它节点的最短距离
print(dis[2])  #从结点1到结点3的最短距离
print(dis[4])  #从结点1到结点5的最短距离


