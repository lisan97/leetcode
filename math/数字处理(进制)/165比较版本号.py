class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        vlist1 = version1.split('.')
        vlist2 = version2.split('.')
        m = len(vlist1)
        n = len(vlist2)
        length = max(m,n)
        i = 0
        while i < length:
            num1 = self.char2int(vlist1[i]) if i < m else 0
            num2 = self.char2int(vlist2[i]) if i < n else 0
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
            else:
                i += 1
        return 0

    def char2int(self,num):
        res = 0
        i = 0
        while i < len(num):
            res += 10 * res + int(num[i])
            i += 1
        return res