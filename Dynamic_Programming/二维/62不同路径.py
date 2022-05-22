class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #状态在i行j列
        #base case:dp[0][:] = 1;dp[:][0] = 1
        #选择：往下或往右
        #状态转移：dp[i][j] = dp[i-1][j] + dp[i][j-1]
        dp = [[1] * n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

#状态压缩
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #状态在i行j列
        #base case:dp[0][:] = 1;dp[:][0] = 1
        #选择：往下或往右
        #状态转移：dp[i][j] = dp[i-1][j] + dp[i][j-1]
        dp = [1] * n
        for i in range(1,m):
            for j in range(1,n):
                dp[j] = dp[j] + dp[j-1]
        return dp[-1]