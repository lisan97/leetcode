class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        self.m = len(grid1)
        self.n = len(grid1[0])
        res = 0
        #如果岛屿 B 中存在一片陆地，在岛屿 A 的对应位置是海水，那么岛屿 B 就不是岛屿 A 的子岛
        #先淹掉所有不是子岛的岛屿
        for i in range(self.m):
            for j in range(self.n):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    self.dfs(grid2,i,j)
        #现在 grid2 中剩下的岛屿都是子岛，计算岛屿数量
        for i in range(self.m):
            for j in range(self.n):
                if grid2[i][j] == 1:
                    res += 1
                    self.dfs(grid2,i,j)
        return res

    def dfs(self,grid,i,j):
        if i < 0 or j < 0 or i >= self.m or j >= self.n:
            #超出索引边界
            return
        if grid[i][j] == 0:
            #已经是海水了
            return
        grid[i][j] = 0
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j-1)