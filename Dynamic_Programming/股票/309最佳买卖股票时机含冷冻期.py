class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
        买入要依赖i-2的状态
        dp[i][1] = max(dp[i-1][1],dp[i-2][0]-prices[i])
        base case:
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
                dp[i][1] = -prices[i]
                continue
            if i - 2 == -1:
                #base case 2
                dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
                #i - 2 小于 0 时根据状态转移方程推出对应 base case
                dp[i][1] = max(dp[i-1][1],-prices[i])
                continue
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-2][0]-prices[i])
        return dp[-1][0]

#状态压缩
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 1:
            return 0
        dp_0 = 0
        dp_1 = float('-inf')
        #存dp[i-2][0]的值
        pre_dp_0 = 0
        for i in range(n):
            tmp = dp_0
            #dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp_0 = max(dp_0,dp_1+prices[i])
            #dp[i][1] = max(dp[i-1][1],dp[i-2][0]-prices[i])
            dp_1 = max(dp_1,pre_dp_0-prices[i])
            pre_dp_0 = tmp
        return dp_0