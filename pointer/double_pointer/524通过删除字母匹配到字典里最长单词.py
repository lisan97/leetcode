class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        self.m = len(s)
        res = ""
        length = 0
        for c in dictionary:
            n = len(c)
            if self.isMatch(s,c,n):
                if n > length:
                    length = n
                    res = c
                elif n == length:
                    #比较字母序
                    if c < res:
                        res = c
                else:
                    continue
        return res

    def isMatch(self,s,p,n):
        i = 0
        j = 0
        while i < self.m and j < n:
            if s[i] == p[j]:
                j += 1
            i += 1
        if j == n:
            return True