class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 状态：i,j的位置
        # 选择：p[j]匹配几个字符
        # dp(i,j)代表s[i..]可以匹配p[j..]
        # base case:j==len(p)和i==len(s)
        # 状态转移逻辑：看s[i] == p[j]，再看j+1是否是*
        self.m = len(s)
        self.n = len(p)
        self.memo = {}
        return self.dp(s, 0, p, 0)

    def dp(self, s, i, p, j):
        if j == self.n:
            return i == self.m
        if i == self.m:
            # 如果能匹配空串，一定是字符和 * 成对儿出现
            if (self.n - j) % 2 == 1:
                return False
            # 检查是否为 x*y*z* 这种形式
            for x in range(j, self.n - 1, 2):
                if p[x + 1] != '*':
                    return False
            return True
        key = str(i) + '_' + str(j)
        if key in self.memo:
            return self.memo[key]
        res = False
        # 匹配
        if s[i] == p[j] or p[j] == '.':
            # 1.1 通配符匹配 0 次或多次
            if j < self.n - 1 and p[j + 1] == '*':
                res = self.dp(s, i, p, j + 2) or self.dp(s, i + 1, p, j)
            # 1.2 常规匹配 1 次
            else:
                res = self.dp(s, i + 1, p, j + 1)
        # 不匹配
        else:
            # 2.1 通配符匹配 0 次
            if j < self.n - 1 and p[j + 1] == '*':
                res = self.dp(s, i, p, j + 2)
            # 2.2 无法继续匹配
            else:
                return False
        self.memo[key] = res
        return self.memo[key]

#迭代
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #dp[i][j]示以 i 截止的字符串是否可以被以 j 截止的正则表达式匹配
        #base case:dp[0][0] = True,还没开始时当然是能匹配的
        m = len(s)
        n = len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(1,n+1):
            #当i还没开始时，遇到*则只能匹配0次
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]
        for i in range(1,m+1):
            for j in range(1,n+1):
                #遇到p[j]为'.'的情况
                if p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                #遇到p[j]为字符的情况，则看这两个字符是否相等
                elif p[j-1] != '*' :
                    dp[i][j] = dp[i-1][j-1] and p[j-1] == s[i-1]
                #p[j]为*，但p[j-1] != s[i]的情况，则只能选择匹配0次
                elif p[j-2] != s[i-1] and p[j-2] != '.':
                    dp[i][j] = dp[i][j-2]
                #p[j]为*，且p[j-1] == s[i]的情况
                # 则匹配1次(dp[i][j-1]),意思是承接以 i 截止的字符串和以 j-1 截止的正则表达式的匹配状态
                # 匹配多次(dp[i-1][j]),因为是匹配多次，所以看以 i-1 截止的字符串和以 j 截止的正则表达式是否匹配
                # 匹配0次(dp[i][j-2])，意思是承接以 i 截止的字符串和以 j-2 截止的正则表达式的匹配状态
                else:
                    dp[i][j] = dp[i][j-1] or dp[i-1][j] or dp[i][j-2]
        return dp[-1][-1]