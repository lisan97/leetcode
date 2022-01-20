from heapq import *
class Prim(object):
    def __init__(self,graph):
        #储「横切边」的优先级队列
        self.pq = heapify([])
        #记录最小生成树的权重和
        self.weithSum = 0
        #图中有 n 个节点
        self.n = len(graph)
        #类似 visited 数组的作用，记录哪些节点已经成为最小生成树的一部分
        self.inMST = [False] * self.n
        #graph 是用邻接表表示的一幅图，
        #graph[s] 记录节点 s 所有相邻的边，
        #三元组 int[]{from, to, weight} 表示一条边
        self.graph = graph

    def Prim(self):
        #从节点 0 开始
        self.cut(0)
        self.inMST[0] = True
        #不断进行切分，向最小生成树中添加边
        while self.pq:
            edge = heappop(self.pq)
            to = edge[1]
            weight = edge[2]
            #节点 to 已经在最小生成树中，跳过
            if not self.inMST[to]:
                #将边 edge 加入最小生成树
                self.weithSum += weight
                self.inMST[to] = True
                #点 to 加入后，进行新一轮切分，会产生更多横切边
                self.cut(to)

    #将 s 的横切边加入优先队列
    def cut(self,s):
        for edge in self.graph[s]:
            to = edge[1]
            #相邻接点 to 已经在最小生成树中，跳过,否则这条边会产生环
            if not self.inMST[to]:
                #加入横切边队列
                heappush(self.pq, edge)

    #最小生成树的权重和
    def WeithSum(self):
        return self.weithSum

    #判断最小生成树是否包含图中的所有节点
    def allConnected(self):
        return sum(self.inMST) == self.n

    def __call__(self):
        self.Prim()