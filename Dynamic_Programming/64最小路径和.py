class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        状态：路径数字和
        选择：往下还是往右
        dp[i][j]代表从左上角到(i,j)的最小路径和
        base case：dp[0][0]=grid[0][0]
        根据选择，状态转移的逻辑:dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]，需注意左边第一列和上面第一行的特殊情况
        '''
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*(n) for _ in range(m)]
        dp[0][0] = grid[0][0]
        #无法从左侧得到
        for i in range(1,m):
            dp[i][0] = grid[i][0]+dp[i-1][0]
        #无法从上得到
        for i in range(1,n):
            dp[0][i] = grid[0][i]+dp[0][i-1]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]