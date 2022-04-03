class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        #base case，对角线为1，因为s[i]=s[i]
        for i in range(n):
            dp[i][i] = 1
        #想求dp[i][j]需要知道dp[i+1][j-1]，dp[i+1][j]，dp[i][j-1]这三个位置反着遍历，为了保证每次计算dp[i][j]时，左、左下、下三个位置已经计算出来，需要反着遍历
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                #s[i]和s[j]一定在最长回文子序列中
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                #若不等，它俩不可能同时出现在最长回文子序列中，则把它俩分别加入s[i+1：j-1]中看哪个生成的回文子序列长
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][-1]

#二维状态压缩
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [1] * n
        for i in range(n-1,-1,-1):
            #存储 dp[i+1][j-1] 的变量
            pre = 0
            for j in range(i+1,n):
                temp = dp[j]
                if s[i] == s[j]:
                    #dp[i][j] = dp[i+1][j-1] + 2
                    dp[j] = pre + 2
                else:
                    dp[j] = max(dp[j],dp[j-1])
                #到下一轮循环，pre 就是 dp[i+1][j-1] 了
                pre = temp
        return dp[-1]

if __name__ == '__main__':
    s = "bbbab"
    #4
    S = Solution()
    print(S.longestPalindromeSubseq(s))