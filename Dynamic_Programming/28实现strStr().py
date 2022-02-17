#暴力解法
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        for i in range(0,n-m+1):
            if haystack[i:i+m] == needle:
                return i
        return -1

#KMP算法
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        if m > n:
            return -1
        if m == n:
            if haystack == needle:
                return 0
            else:
                return -1
        if not needle:
            return 0
        # dp[状态][字符] = 下个状态
        dp = [[0] * 256 for _ in range(m)]
        # base case，只有遇到 pat[0] 这个字符才能使状态从 0 转移到 1
        dp[0][ord(needle[0])] = 1
        # 影子状态 X 初始为 0
        X = 0
        for j in range(1, m):
            for c in range(256):
                if chr(c) == needle[j]:
                    dp[j][c] = j + 1
                else:
                    dp[j][c] = dp[X][c]
            # 更新影子状态，在 pat 中匹配 pat[1..end]
            X = dp[X][ord(needle[j])]

        j = 0
        for i in range(n):
            # 计算 pat 的下一个状态
            j = dp[j][ord(haystack[i])]
            # 到达终止态，返回结果
            if j == m:
                return i - m + 1
        # 没到达终止态，匹配失败
        return -1