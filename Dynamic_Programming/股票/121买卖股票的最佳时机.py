class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #状态：天,最大交易限制次数,是否持有股票
        #选择：买,卖,持有
        #dp[i][k][0/1]：在i天，最大交易限制为k次，是否持有股票的最大利润
        #base case:dp[-1][:][0] = dp[:][0][0] = 0
        #          dp[-1][:][1] = dp[:][0][1] = -float('inf)
        #转移逻辑：dp[i][1][0] = max(dp[i-1][1][0],dp[i-1][1][1]+price[i])
        #         dp[i][1][1] = max(dp[i-1][1][1],dp[i-1][0][0]-price[i]) = max(dp[i-1][1][1],-price[i])
        #在这个问题上：k=1可以直接忽略掉：dp[i][0] = max(dp[i-1][0],dp[i-1][1]+price[i])
        #                              dp[i][1] = max(dp[i-1][1],-price[i])

        n = len(prices)
        dp = [[0]*2  for _ in range(n)]
        for i in range(n):
            if i-1==-1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],-prices[i])
        return dp[-1][0]

#状态压缩
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        # 记录截止到现在最大的利润
        dp_0 = 0
        # 记录当前最便宜的买入日期
        dp_1 = float('-inf')
        for i in range(n):
            # dp[i][0] = max(dp[i-1][0],dp[i-1][1]+price[i])
            dp_0 = max(dp_0, dp_1 + prices[i])
            # dp[i][1] = max(dp[i-1][1],-price[i])
            dp_1 = max(dp_1, -prices[i])
        return dp_0


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))