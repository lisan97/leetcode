class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        '''
        状态第i个数
        dp[i]代表前i个数有几种翻译方法
        dp[i] = dp[i-1]+dp[i-2] if num[i-1:i+1] <= 25 and num[i-1] = 0
        否则dp[i] = dp[i-1]
        dp[i-1]代表num[i]自成一个数字,dp[i-2]代表num[i]和num[i-1]结合起来组成一个数
        '''
        s = str(num)
        n = len(s)
        if n < 2:
            return n
        dp = [0] * n
        dp[0] = 1
        if s[0] != '0' and int(s[:2]) <= 25:
            dp[1] = 2
        else:
            dp[1] = 1
        for i in range(2,n):
            if s[i-1] != '0' and int(s[i-1:i+1]) <= 25:
                dp[i] = dp[i-1]+dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[-1]