class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.m = len(grid)
        self.n = len(grid[0])
        res = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    #淹没岛屿，并更新最大岛屿面积
                    res = max(res,self.dfs(grid,i,j))
        return res

    def dfs(self,grid,i,j):
        if i < 0 or j < 0 or i >= self.m or j >= self.n:
            #超出索引边界
            return 0
        if grid[i][j] == 0:
            #已经是海水了
            return 0
        grid[i][j] = 0
        #该岛屿的面积等于他四周岛屿面积+1
        return self.dfs(grid,i+1,j)+self.dfs(grid,i,j+1)+self.dfs(grid,i-1,j)+self.dfs(grid,i,j-1)+1