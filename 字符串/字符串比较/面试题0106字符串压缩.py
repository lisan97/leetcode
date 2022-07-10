class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ''
        cur = S[0]
        curnum = 1
        res = ''
        n = len(S)
        for i in range(1,n):
            if cur != S[i]:
                res = res + cur + str(curnum)
                cur = S[i]
                curnum = 1
            else:
                curnum += 1
        res = res + cur + str(curnum)
        return res if len(res) < n else S