class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n = len(coins)
        #若只使用 coins 中的前 i 个硬币的面值，若想凑出金额 j，有 dp[i][j] 种凑法。
        dp = [[0]*(amount+1) for _ in range(n+1)]
        #dp[..][0] = 1,如果凑出的目标金额为 0，那么“无为而治”就是唯一的一种凑法
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1,n+1):
            for j in range(1,amount+1):
                #如果你不把这第 i 个物品装入背包,dp[i][j] 应该等于 dp[i][j-coins[i-1]]
                #如果你把这第 i 个物品装入了背包,dp[i][j] 应该等于 dp[i][j-coins[i-1]]
                #而我们想求的 dp[i][j] 是「共有多少种凑法」，所以 dp[i][j] 的值应该是以上两种选择的结果之和
                if j >= coins[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

#降维
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n = len(coins)
        dp = [0] * (amount+1)
        dp[0] = 1
        for i in range(n):
            for j in range(1,amount+1):
                if j >= coins[i]:
                    dp[j] = dp[j] + dp[j-coins[i]]
        return dp[-1]