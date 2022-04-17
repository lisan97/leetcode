class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        从字符串的每个位置开始，向左向右延长，判断存在多少以当前位置为中轴的回文子字符串。
        '''
        self.n = len(s)
        self.s = s
        res = 0
        for i in range(self.n):
            res += self.countPalind(i,i)#奇数长度
            res += self.countPalind(i,i+1)# 偶数长度
        return res

    def countPalind(self,i,j):
        count = 0
        while i >= 0 and j < self.n and self.s[i] == self.s[j]:
            count += 1
            i -= 1
            j += 1
        return count