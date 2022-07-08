class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #dp[i][j](i,j)离陆地的最近距离
        m = len(grid)
        n = len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = min(dp[i][j],dp[i-1][j]+1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j],dp[i][j-1]+1)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if grid[i][j] == 0:
                    if i < m-1:
                        dp[i][j] = min(dp[i][j],dp[i+1][j]+1)
                    if j < n-1:
                        dp[i][j] = min(dp[i][j],dp[i][j+1]+1)
                    res = max(dp[i][j],res)
        return res if res not in [float('inf'),0] else -1