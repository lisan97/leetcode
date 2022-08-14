class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)
        #base case: dp[0][..] = dp[..][0] = 0
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                #根据 s1[i] 和 s2[j] 的情况做选择
                if text1[i-1] == text2[j-1]:
                    #s1[i-1] 和 s2[j-1] 必然在 lcs 中
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    #s1[i] 和 s2[j] 至少有一个不在 lcs 中
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]