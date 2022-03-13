class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n in [0,1]:
            return 0
        #有效的限制 k 应该不超过 n/2
        k = min(k, n // 2)
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

        
        
if __name__ == '__main__':
    k=2
    prices=[2, 4, 1]
    print(Solution().maxProfit(k,prices))