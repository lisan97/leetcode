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