#递归
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #dp 数组全都初始化为特殊值
        self.memo = [-666]*(amount + 1)
        return self.dp(coins,amount)

    def dp(self,coins,amount):
        #base case
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        #查备忘录，防止重复计算
        if self.memo[amount] != -666:
            return self.memo[amount]
        res = float('inf')
        for coin in coins:
            #计算子问题的结果
            subproblem = self.dp(coins,amount-coin)
            #子问题无解则跳过
            if subproblem == -1:
                continue
            #在子问题中选择最优解，然后加一
            res = min(res,subproblem+1)
        #把计算结果存入备忘录
        self.memo[amount] = res if res != float('inf') else -1
        return self.memo[amount]

#迭代
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #数组大小为 amount + 1，初始值也为 amount + 1
        dp = [amount+1]*(amount+1)
        #base case
        dp[0] = 0
        #外层 for 循环在遍历所有状态的所有取值
        for i in range(1,amount+1):
            #内层 for 循环在求所有选择的最小值
            for coin in coins:
                #子问题无解，跳过
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i],dp[i-coin]+1)
        return dp[-1] if dp[-1] != amount+1 else -1