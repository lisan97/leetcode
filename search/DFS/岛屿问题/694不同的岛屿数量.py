class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        islands = set()
        self.m = len(grid)
        self.n = len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    #淹掉这个岛屿，同时存储岛屿的序列化结果
                    track = []
                    #初始的方向可以随便写，不影响正确性
                    self.dfs(grid,i,j,track,6)
                    islands.add(','.join(track))
        return len(islands)
    
    def dfs(self,grid,i,j,track,dir):
        if i < 0 or j < 0 or i >= self.m or j >= self.n:
            return
        if grid[i][j] == 0:
            return
        #前序遍历位置：进入 (i, j)
        track.append(str(dir))
        grid[i][j] = 0
        self.dfs(grid,i-1,j,track,1) #上
        self.dfs(grid, i + 1, j, track, 2) #下
        self.dfs(grid, i, j-1, track, 3) #左
        self.dfs(grid, i, j+1, track, 4) #右
        #后序遍历位置：离开 (i, j)
        track.append(str(-dir))
        
if __name__ == '__main__':
    grid = [[1,1,0,1,1],
            [1,0,0,0,0],
            [0,0,0,0,1],
            [1,1,0,1,1]]
    print(Solution().numDistinctIslands(grid))