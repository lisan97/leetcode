class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        from heapq import *
        graph = self.buildGraph(n,edges,succProb)
        disTo = [0] * n
        pq = []
        heapify(pq)
        #因为python只有小顶堆，因而将所有概率变为负，最后返回结果时再取正
        disTo[start] = -1
        heappush(pq,(-1,start))
        while pq:
            prob, cur = heappop(pq)
            if cur == end:
                return -disTo[end]
            if prob > disTo[cur]:
                continue
            for edge in graph[cur]:
                nextprob,nextNode = edge[0], edge[1]
                #边和边之间是乘法关系
                disToNextNode = - abs(disTo[cur] * nextprob)
                if disToNextNode < disTo[nextNode]:
                    disTo[nextNode] = disToNextNode
                    heappush(pq,(disToNextNode,nextNode))
        return 0

    def buildGraph(self,n,edges,succProb):
        graph = [[] for _ in range(n)]
        for edge,prob in zip(edges,succProb):
            graph[edge[0]].append([-prob,edge[1]])
            graph[edge[1]].append([-prob,edge[0]])
        return graph