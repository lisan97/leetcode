class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #在字符串的第i位
        #自成一个字母，或是和前一个数字一起成为一个字母
        #dp[i]在字符串第i位的解码总数
        #base case:dp[0] = 1 if s[0] != '0'
        #状态转移 需要考虑：数字 0 或者当相邻两数字大于 26 时的各种情况
        #开头是0肯定无解
        if s[0] == '0':
            return 0
        n = len(s)
        if n == 1:
            return 1
        dp = [0] * n
        #因为dp[i]依赖dp[i-1]和dp[i-2]，先求出dp[0]和dp[1]
        dp[0] = 1
        #当s[1] = 0时，如果s[0]=0或者前后两个数>26时，无解
        if s[1] == '0' and int(s[0])>2:
            return 0
        #如果s[1] = 0，则前后两个数必须组一起，如果前后两个数>26，那么s[1]只能自成一个字母，这两种情况都只有一种可能性
        elif s[1] == '0' or int(s[0:2])> 26:
            dp[1] = 1
        #s[0]和s[1]可以组在一起，也可以分开各自成为一个数
        else:
            dp[1] = 2
        for i in range(2,n):
            #当s[i] = 0时，如果s[i-1]=0或者前后两个数>26时，无解
            if (s[i-1] == '0' or int(s[i-1]) > 2) and s[i] == '0':
                return 0
            #当s[i-1] = 0或者前后两个数>26，那么s[i]只有自成一个字母这一种可能，则dp[i]=dp[i-1]
            if s[i-1] == '0' or int(s[i-1:i+1]) > 26:
                dp[i] = dp[i-1]
            #如果s[i] = 0，那么s[i-1]和s[i]必须组成一个数，所以dp[i] = dp[i-2]
            elif s[i] == '0':
                dp[i] = dp[i-2]
            #s[i-1]可以和s[i]必须组成一个数，也可以各自成为一个字母，因此dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]