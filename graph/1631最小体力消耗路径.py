class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        from heapq import *
        m = len(heights)
        n = len(heights[0])
        #定义：从 (0, 0) 到 (i, j) 的最小体力消耗是 effortTo[i][j]
        #dp table 初始化为正无穷
        disTo = [[float('inf') for _ in range(n)] for _ in range(m)]
        #优先级队列，effortFromStart 较小的排在前面
        pq = []
        heapify(pq)
        #base case，起点到起点的最小消耗就是 0
        disTo[0][0] = 0
        #从起点 (0, 0) 开始进行 BFS
        heappush(pq,(0,0,0))
        while pq:
            weight, curx, cury = heappop(pq)
            #到达终点提前结束
            if curx == m-1 and cury == n-1:
                return disTo[m-1][n-1]
            if weight > disTo[curx][cury]:
                continue
            #将 (curX, curY) 的相邻坐标装入队列
            for nextNode in self.adj(curx,cury,heights):
                nextx,nexty = nextNode[0],nextNode[1]
                #计算从 (curX, curY) 达到 (nextX, nextY) 的消耗
                disTonextNode = max(disTo[curx][cury],self.weight(curx,cury,nextx,nexty,heights))
                if disTonextNode < disTo[nextx][nexty]:
                    #更新 dp table
                    disTo[nextx][nexty] = disTonextNode
                    heappush(pq,(disTonextNode,nextx,nexty))

    def adj(self,x,y,heights):
        m = len(heights)
        n = len(heights[0])
        #方向数组，上下左右的坐标偏移量
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        neighbors = []
        #返回坐标 (x, y) 的上下左右相邻坐标
        for dir in dirs:
            nx = x + dir[0]
            ny = y + dir[1]
            #索引越界
            if nx >= m or nx < 0 or ny >= n or ny < 0:
                continue
            neighbors.append([nx,ny])
        return neighbors

    def weight(self,curx,cury,nextx,nexty,heights):
        return abs(heights[curx][cury]-heights[nextx][nexty])