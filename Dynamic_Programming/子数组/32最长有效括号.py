class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        有效括号一定是以)结尾的
        dp[i]代表以s[i]结尾的连续最长有效括号
        状态转移:当dp[i-1] = '('时：dp[i] = dp[i-2] + 2
        当dp[i-1] = ')'时，则需要看dp[i-dp[i-1]-1]是否是'('，是的话则i位置对最长有效括号长度为 i-1位置的最长括号长度加上当前位置新增的2
        同时i−dp[i−1]−1 和i组成了有效括号对，这将是一段独立的有效括号序列，如果之前的子序列是形如(...)这种序列，那么当前位置的最长有效括号长度还需要加上这一段，例：()(()))，所以是：
        dp[i]=dp[i−1]+dp[i−dp[i−1]−2]+2
        '''
        if not s:
            return 0
        n = len(s)
        dp = [0] * n
        max_res = 0
        for i in range(1,n):
            if s[i] == ')':
                if s[i-1] == '(':
                    if i - 2 >= 0:
                        dp[i] = dp[i-2] + 2
                    else:
                        dp[i] = 2
                    max_res = max(max_res,dp[i])
                else:
                    if i - dp[i-1] - 1 >= 0 and s[i-dp[i-1]-1] == '(':

                        if i-dp[i-1]-2 >= 0:
                            dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
                        else:
                            dp[i] = dp[i-1] + 2
                        max_res = max(max_res,dp[i])
        return max_res