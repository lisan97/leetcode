class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #状态：现在在第几阶楼梯
        #选择：爬1阶还是2阶
        #dp[i]在第i阶楼梯有几种方法
        #base case:dp[0] = 0,dp[1]=1,dp[2]=2
        #状态转移：dp[i] = dp[i-1]+dp[i-2]
        if n < 3:
            return n
        dp = [0] * (n)
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]

#状态压缩
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        dp_2 = 1
        dp_1 = 2
        for i in range(2,n):
            dp = dp_1+dp_2
            dp_2 = dp_1
            dp_1 = dp
        return dp