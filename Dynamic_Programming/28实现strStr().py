#暴力解法 时间复杂度：O(n×m)
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

#暴力解法
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        '''
        让字符串needle 与字符串haystack的所有长度为m的子串均匹配一次
        '''
        n = len(haystack)
        m = len(needle)
        if m > n:
            return -1
        if m == n:
            if haystack == needle:
                return 0
            else:
                return -1
        for i in range(n-m+1):
            found = True
            for j in range(m):
                #为了减少不必要的匹配，我们每次匹配失败即立刻停止当前子串的匹配，对下一个子串继续匹配。
                if needle[j] != haystack[i+j]:
                    found = False
                    break
            #如果当前子串匹配成功，我们返回当前子串的开始位置即可
            if found:
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
        nex = self.getnext(needle)
        m = len(haystack)
        n = len(needle)
        j = -1 #因为next数组里记录的起始位置为-1
        for i in range(m): #注意i就从0开始
            while j >=0 and haystack[i] != needle[j+1]: #不匹配
                j = nex[j] #j 寻找之前匹配的位置
            if haystack[i] == needle[j+1]: #匹配，j和i同时向后移动
                j += 1 #i的增加在for循环里
            if j == n-1: #文本串s里出现了模式串t
                return i - n + 1 #返回此时文本串的开头
        return -1

    def getnext(self,needle):
        n = len(needle)
        nex = [-1]*n
        j = -1
        for i in range(1,n): #注意i从1开始
            while j >= 0 and needle[i] != needle[j+1]: #前后缀不相同
                j = nex[j] #向前回溯
            if needle[i] == needle[j+1]: #找到相同的前后缀
                j += 1
            nex[i] = j #将j（前缀的长度）赋给next[i]
        return nex

#labuladong KMP算法 复杂度较高
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