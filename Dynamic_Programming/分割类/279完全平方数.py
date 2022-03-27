class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        状态：在第个数
        选择：用哪个完全平方数
        dp[i]代表整数i的最少数量
        base case:dp[0]=0
        状态转移:dp[i] = 1 + min(dp[i-1], dp[i-4], dp[i-9] · · · )
        '''
        dp = [n+1]*(n+1)
        dp[0] = 0
        for i in range(1,n+1):
            num = int(i**0.5)
            for j in range(1,num+1):
                dp[i] = min(dp[i],dp[i-j**2]+1)
        return dp[-1]