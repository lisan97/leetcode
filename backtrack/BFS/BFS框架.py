from collections import deque
#计算从起点 start 到终点 target 的最近距离
def BFS(start, target):
    visited = set([start]) #避免走回头路
    q = deque([start]) #核心数据结构
    step = 0 #记录扩散的步数
    while q:
        sz = len(q)
        #将当前队列中的所有节点向四周扩散
        for _ in range(sz):
            node = q.popleft()
            #划重点：这里判断是否到达终点
            if node == target:
                return step
            #将 cur 的相邻节点加入队列
            for x in node.adj():
                if x not in visited:
                    q.append(x)
                    visited.add(x)
        #划重点：更新步数在这里
        step += 1
    #没找到，返回-1
    return -1

