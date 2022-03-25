class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        先像岛屿问题一样用dfs找到其中一个岛并标记
        然后用bfs找到另一个岛的最短路径
        '''
        from collections import deque
        self.directions = [-1,0,1,0,-1]
        self.m = len(grid)
        self.n = len(grid[0])
        points = deque([])
        first = False
        for i in range(self.m):
            if first:
                break
            for j in range(self.n):
                if grid[i][j] == 1:
                    self.dfs(grid,i,j,points)
                    first = True
                    break
        step = 1
        while points:
            sz = len(points)
            for _ in range(sz):
                i,j = points.popleft()
                for a in range(4):
                    x = i + self.directions[a]
                    y = j + self.directions[a+1]
                    if x >= 0 and x < self.m and y >= 0 and y < self.n:
                        if grid[x][y] == 2:
                            continue
                        elif grid[x][y] == 1:
                            return step
                        else:
                            points.append([x,y])
                            grid[x][y] = 2
            step += 1
        return 0



    def dfs(self,grid,i,j,points):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or grid[i][j] == 2:
            return
        if grid[i][j] == 0:
            points.append([i,j])
            return
        grid[i][j] = 2
        for a in range(4):
            x = i + self.directions[a]
            y = j + self.directions[a+1]
            self.dfs(grid,x,y,points)
        # self.dfs(grid,i-1,j,points)
        # self.dfs(grid,i+1,j,points)
        # self.dfs(grid,i,j-1,points)
        # self.dfs(grid,i,j+1,points)