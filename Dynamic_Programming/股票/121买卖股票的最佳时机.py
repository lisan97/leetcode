class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 1:
            return 0
        #记录当前最便宜的买入日期
        buy = -prices[0]
        #记录截止到现在最大的利润
        profit = 0
        for i in range(1,n):
            buy = max(buy,-prices[i])
            profit = max(profit,prices[i]+buy)
        return profit