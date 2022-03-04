class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = '#'+'#'.join(list(s))+'#'
        res = ''
        maxlength = 0
        self.n = len(s)
        for i in range(self.n):
            if i < (maxlength-1)/2 or (self.n-i) < (maxlength-1)/2:
                break
            tmp = self.find(s,i)
            length = len(tmp)
            if length > maxlength:
                res = tmp
                maxlength = length
        return res.replace('#','')

    def find(self,s,i):
        a,b = i,i
        res = ''
        while a >=0 and b < self.n:
            if s[a] == s[b]:
                res = s[a:b+1]
            else:
                break
            a -= 1
            b += 1
        return res