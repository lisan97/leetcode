class Solution(object):
    def dicesProbability(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        '''
        当添加骰子的点数为 1 时，前n−1 个骰子的点数和应为j−1 ，方可组成点数和 j ；
        同理，当此骰子为 2 时，前n−1 个骰子应为j−2 ；
        以此类推，直至此骰子点数为 6 。将这 6 种情况的概率相加再除以6
        '''
        #状态：前i个筛子，和为j
        #dp[i][j]表示前i个筛子，和为j的概率
        #和最小为n，最大为6n，5n+1种可能
        #base case: i = 1; dp[1][1:6] = 1
        #状态转移：dp[i][j] = (dp[i-1][j-1] + ... + dp[i-1][j-6]) / 6 注意不能越界
        res = [0] * (5*n+1)
        dp = [[0] * (6*n+1) for _ in range(n+1)]
        for j in range(1,7):
            dp[1][j] = 1/6.0
        for i in range(2,n+1):
            for j in range(i,6*i+1):
                for k in range(1,7):
                    #防止越界
                    if j - k <= 0:
                        break
                    else:
                        dp[i][j] += dp[i-1][j-k] / 6.0
        for j in range(5*n+1):
            res[j] = dp[n][j+n]
        return res