class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        #状态i行j列
        #dp[i][j]以(i,j)为右下角的正方形的边长
        #状态转移：dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
        m = len(matrix)
        n = len(matrix[0])
        #针对第一行和第一列的情况多加1行和1列
        dp = [[0]*(n+1) for _ in range(m+1)]
        max_side = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                    max_side = max(max_side,dp[i][j])
        return max_side ** 2