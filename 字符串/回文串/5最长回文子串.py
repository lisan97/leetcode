class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #头尾以及每两个字符中间添加一个特殊字符 #原先长度为偶数的回文字符串会变成长度为奇数的回文字符串
        s = '#'+'#'.join(list(s))+'#'
        res = ''
        maxlength = 0
        self.n = len(s)
        for i in range(self.n):
            #1. 已无法超过最长的长度
            if i < (maxlength-1)/2 or (self.n-i) < (maxlength-1)/2:
                break
            tmp = self.palindrome(s,i)
            length = len(tmp)
            if length > maxlength:
                res = tmp
                maxlength = length
        return res.replace('#','')

    def palindrome(self,s,i):
        l,r = i,i
        while l >=0 and r < self.n and s[l] == s[r]:
            l -= 1
            r += 1
        #返回以 s[l] 和 s[r] 为中心的最长回文串
        return s[l+1:r]