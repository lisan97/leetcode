class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return " "
        arr = [0] * 256
        for i in range(len(s)):
            n = ord(s[i])-ord('a')
            arr[n] += 1
        for c in s:
            if arr[ord(c)-ord('a')] == 1:
                return c
        return ' '

#一遍遍历
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ' '
        from collections import OrderedDict
        dic = OrderedDict()
        for c in s:
            dic[c] = c not in dic
        for k,v in dic.items():
            if v:
                return k
        return ' '