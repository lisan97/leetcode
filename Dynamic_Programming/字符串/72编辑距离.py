#迭代
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            dp[i][0] = i
        for i in range(1,n+1):
            dp[0][i] = i
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1]+1 #插入 我直接在 s1[i]后插入一个和 s2[j] 一样的字符, 那么 s2[j] 就被匹配了，前移 j，继续跟 i 对比
                                   ,dp[i-1][j]+1 #删除 我直接把 s[i] 这个字符删掉 前移 i，继续跟 j 对比
                                   ,dp[i-1][j-1]+1) #替换 我直接把 s1[i] 替换成 s2[j]，这样它俩就匹配了 同时前移 i，j 继续对比
        return dp[-1][-1]

#递归
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        self.memo = [[-666] * n for _ in range(m)]
        return self.dp(m-1,n-1, word1, word2)


    def dp(self,i,j,word1,word2):
        if i == -1:
            return j+1
        if j == -1:
            return i+1
        if self.memo[i][j] != -666:
            return self.memo[i][j]
        if word1[i] == word2[j]:
            self.memo[i][j] = self.dp(i-1,j-1,word1,word2)
            #return self.dp(i-1,j-1,word1,word2)
        else:
            self.memo[i][j] = min(self.dp(i,j-1,word1,word2)+1,
                                  self.dp(i-1,j,word1,word2)+1,
                                  self.dp(i-1,j-1,word1,word2)+1)
        return self.memo[i][j]

if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    #3
    S = Solution()
    print(S.minDistance(word1, word2))