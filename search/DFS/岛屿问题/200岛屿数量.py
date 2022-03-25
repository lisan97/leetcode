class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        '''
        因为 dfs 函数遍历到值为 0 的位置会直接返回，所以只要把经过的位置都设置为 0，就可以起到不走回头路的作用。
        避免维护 visited 数组。
        '''
        self.m = len(grid)
        self.n = len(grid[0])
        res = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1':
                    #每发现一个岛屿，岛屿数量加一
                    res += 1
                    #然后使用 DFS 将岛屿淹了
                    self.dfs(grid,i,j)
        return res
    #从 (i, j) 开始，将与之相邻的陆地都变成海水
    def dfs(self,grid,i,j):
        if i < 0 or j < 0 or i >= self.m or j >= self.n:
            #超出索引边界
            return
        if grid[i][j] == '0':
            #已经是海水了
            return
        #将 (i, j) 变成海水
        grid[i][j] = '0'
        #淹没上下左右的陆地
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j-1)