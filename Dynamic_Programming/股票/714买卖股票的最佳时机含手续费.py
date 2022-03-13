class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        '''
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
        dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i]-fee)
        base case
        dp[-1][0] = 0
        dp[-1][1] = float('-inf')
        '''
        n = len(prices)
        if n == 1:
            return 0
        dp = [[0]*2 for _ in range(n)]
        for i in range(n):
            if i - 1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i] - fee
                continue
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i]-fee)
        return dp[-1][0]

#状态压缩
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        if n == 1:
            return 0
        dp_0 = 0
        dp_1 = float('-inf')
        for i in range(n):
            dp_0 = max(dp_0,dp_1+prices[i])
            dp_1 = max(dp_1,dp_0-prices[i]-fee)
        return dp_0