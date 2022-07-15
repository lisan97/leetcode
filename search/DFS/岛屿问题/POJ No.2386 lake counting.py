class Solution(object):
    def numlakes(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        '''
        岛屿数量的变种：八连通的积水被认为是在一起的，得朝8个方向去遍历
        '''
        self.m = len(grid)
        self.n = len(grid[0])
        res = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 'w':
                    # 每发现一个积水，积水数量加一
                    res += 1
                    # 然后使用 DFS 将和该积水连通的积水都填满
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= self.m or j >= self.n or grid[i][j] == '.':
            # 超出索引边界 或 已不是积水
            return
        # 将 (i, j) 填满
        grid[i][j] = '.'
        # 填满8个方向的水洼的
        for x in range(-1,2,1):
            for y in range(-1,2,1):
                self.dfs(grid, i + x, j + y)

