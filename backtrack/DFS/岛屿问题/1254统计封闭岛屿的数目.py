class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.m = len(grid)
        self.n = len(grid[0])
        res = 0
        #把靠四周的岛屿都淹掉
        for i in range(self.m):
            self.dfs(grid,i,0)
            self.dfs(grid,i,self.n-1)
        for i in range(self.n):
            self.dfs(grid,0,i)
            self.dfs(grid,self.m-1,i)
        #遍历 grid，剩下的岛屿都是封闭岛屿
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0:
                    res += 1
                    self.dfs(grid,i,j)
        return res

    def dfs(self,grid,i,j):
        if i < 0 or j < 0 or i >= self.m or j >= self.n:
            #超出索引边界
            return
        if grid[i][j] == 1:
            #已经是海水了
            return
        #将 (i, j) 变成海水
        grid[i][j] = 1
        #淹没上下左右的陆地
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j-1)