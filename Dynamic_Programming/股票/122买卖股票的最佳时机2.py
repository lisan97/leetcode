class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 1:
            return 0
        buy = -prices[0]
        profit = 0
        for i in range(1,n):
            #记录当前利润减去买入的成本后还剩多少钱
            buy = max(buy,profit-prices[i])
            profit = max(profit,prices[i]+buy)
        return profit