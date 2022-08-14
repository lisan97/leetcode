class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        #定义：对 s[i..j]，最少需要插入 dp[i][j] 次才能变成回文
        #base case：i == j 时 dp[i][j] = 0，单个字符本身就是回文
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        #从下向上遍历
        for i in range(n-1,-1,-1):
            #从左向右遍历
            for j in range(i+1,n):
                #根据 s[i] 和 s[j] 进行状态转移
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j],dp[i][j-1])+1
        return dp[0][-1]

#状态压缩
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0]*n
        for i in range(n-1,-1,-1):
            pre = 0
            for j in range(i+1,n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = pre
                else:
                    dp[j] = min(dp[j],dp[j-1])+1
                pre = temp
        return dp[-1]