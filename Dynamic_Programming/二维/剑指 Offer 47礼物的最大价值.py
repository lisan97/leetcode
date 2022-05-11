class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]

#状态压缩
class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = grid[i][j]
                elif i == 0:
                    dp[j] = dp[j-1] + grid[i][j]
                elif j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = max(dp[j-1],dp[j])+grid[i][j]
        return dp[-1]