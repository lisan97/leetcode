from heapq import *
def dijkstra(start,graph):
    n = len(graph)
    #记录最短路径的权重，你可以理解为 dp table
    #定义：distTo[i] 的值就是节点 start 到达节点 i 的最短路径权重
    #求最小值，所以 dp table 初始化为正无穷
    disTo = [float('inf')] * n
    #base case，start 到 start 的最短距离就是 0
    disTo[start] = 0
    pq = []
    #优先级队列，distFromStart 较小的排在前面
    heapify(pq)
    heappush(pq,(0,start))
    while pq:
        curDist,curNode = heappop(pq)
        if curDist > disTo[curNode]:
            #已经有一条更短的路径到达 curNode 节点了
            continue
        #将 curNode 的相邻节点装入队列
        for edge in graph[curNode]:
            weight, nextNode = edge[0], edge[1]
            #看看从 curNode 达到 nextNode 的距离是否会更短
            distToNextNode = disTo[curNode] + weight
            if distToNextNode < disTo[nextNode]:
                #更新 dp table
                disTo[nextNode] = distToNextNode
                #将这个节点以及距离放入队列
                heappush(pq,(distToNextNode,nextNode))
    return disTo