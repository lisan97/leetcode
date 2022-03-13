class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        转移：
        dp[i][k][0] = max(dp[i-1][k][0],dp[i-1][k][1]+prices[i])
        dp[i][k][1] = max(dp[i-1][k][1],dp[i-1][k-1][0]-prices[i])
        base case:
        dp[-1][:][0] = dp[:][0][0] = 0
        dp[-1][:][1] = dp[:][0][1] = float('-inf')
        '''
        n = len(prices)
        if n == 1:
            return 0
        k = 2
        dp = [[[0] * 2 for _ in range(k+1)] for _ in range(n)]
        for i in range(n):
            for j in range(k,0,-1):
                if i - 1 == -1:
                    ##dp[-1][:][1]的情况都出现在这，因为k最小遍历到1，那么dp[:][0][1]的情况出现不了
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                    continue
                dp[i][j][0] = max(dp[i-1][j][0],dp[i-1][j][1]+prices[i])
                dp[i][j][1] = max(dp[i-1][j][1],dp[i-1][j-1][0]-prices[i])
        return dp[n-1][k][0]

#状态压缩
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        转移：
        dp[i][2][0] = max(dp[i-1][2][0],dp[i-1][2][1]+prices[i])
        dp[i][2][1] = max(dp[i-1][2][1],dp[i-1][1][0]-prices[i])
        dp[i][1][0] = max(dp[i-1][1][0],dp[i-1][1][1]+prices[i])
        dp[i][1][1] = max(dp[i-1][1][1],-prices[i])
        base case:
        dp[-1][:][0] = dp[:][0][0] = 0
        dp[-1][:][1] = dp[:][0][1] = float('-inf')
        '''
        n = len(prices)
        if n == 1:
            return 0
        dp_10 = 0
        dp_11 = float('-inf')
        dp_20 = 0
        dp_21 = float('-inf')
        for i in range(n):
            #second sell
            #dp[i][2][0] = max(dp[i-1][2][0],dp[i-1][2][1]+prices[i])
            dp_20 = max(dp_20,dp_21+prices[i])
            #second buy
            #dp[i][2][1] = max(dp[i-1][2][1],dp[i-1][1][0]-prices[i])
            dp_21 = max(dp_21,dp_10-prices[i])
            #first sell
            #dp[i][1][0] = max(dp[i-1][1][0],dp[i-1][1][1]+prices[i])
            dp_10 = max(dp_10,dp_11+prices[i])
            #first buy
            #dp[i][1][1] = max(dp[i-1][1][1],-prices[i])
            dp_11 = max(dp_11,-prices[i])
        return dp_20

if __name__ == '__main__':
    prices=[3,3,5,0,0,3,1,4]
    print(Solution().maxProfit(prices))