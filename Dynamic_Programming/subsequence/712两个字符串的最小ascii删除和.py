#正向思维求删除最小和
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for i in range(1,n+1):
            dp[0][i] = dp[0][i-1] + ord(s2[i-1])
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+ord(s1[i-1]),dp[i][j-1]+ord(s2[j-1]))
        return dp[-1][-1]

#逆向思维求最长公共子序列
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        #删除的结果就是最长公共子序列
        #当有多种最长公共子序列可能的时候，应选择ascii更大的公共子序列--这样删除的ascii会更小
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + ord(s1[i-1])
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        total = 0
        for c in s1:
            total += ord(c)
        for c in s2:
            total += ord(c)
        #最后拿两个字符串的ascii和减去2倍最长公共子序列ascii和即可
        return total - 2*dp[-1][-1]