class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        #i,j
        #dp[i][j]s的前i个字符，包含t的前j个字符的数量
        #base case:dp[0][:] = 0;dp[:][0] = 1
        #状态转移dp[i][j] = dp[i-1][j] if s[i] != t[j] #只能用s[:i-1]去匹配t[:j]了
        #       dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i] = t[j] #可以选择用s[:i-1]去匹配t[:j]，也可以选择用s[i]匹配t[j]，然后看s[:i-1]和t[:j-1]匹配的情况
        m = len(s)
        n = len(t)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = 0
                else:
                    if s[i-1] == t[j-1]:
                        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j]
        return dp[-1][-1]