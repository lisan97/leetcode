class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #k无限制->k为正无穷
        #转移
        #dp[i][k][0] = max(dp[i-1][k][0],dp[i-1][k][1]+prices[i])
        #dp[i][k][1] = max(dp[i-1][k][1],dp[i-1][k-1][0]-prices[i]) = max(dp[i-1][k][1],dp[i-1][k][0]-prices[i])
        #那么有没有k并不重要，可以简化为：
        #dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
        #dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
        #base case
        #dp[-1][:][0] = dp[:][0][0] = 0
        #dp[-1][:][1] = dp[:][0][1] = float('-inf')
        #转化为：
        #dp[-1][0]  = 0
        #dp[-1][1] = float('-inf')
        n = len(prices)
        k = n
        if n == 1:
            return 0
        dp = [[0]*2 for _ in range(n)]
        for i in range(n):
            if i - 1==-1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
        return dp[-1][0]

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        k = n
        if n == 1:
            return 0
        #记录截止到现在最大的利润
        dp_0 = 0
        #记录当前利润减去买入的成本后还剩多少钱
        dp_1 = float('-inf')
        for i in range(n):
            #dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp_0 = max(dp_0,dp_1+prices[i])
            #dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
            dp_1 = max(dp_1,dp_0-prices[i])
        return dp_0

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))