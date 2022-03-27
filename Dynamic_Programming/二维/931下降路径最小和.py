class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        dp = [[float('inf')]*n for _ in range(n)]
        for i in range(n):
            dp[0][i] = matrix[0][i]
        for i in range(1,n):
            for j in range(n):
                if j == 0:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j],dp[i-1][j+1])
                elif j == n-1:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j-1],dp[i-1][j])
                else:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])
        return min(dp[-1])