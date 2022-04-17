class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        isone = False
        length = 0
        for v in dic.values():
            if v % 2:
                if not isone:
                    length += v
                    isone = True
                else:
                    length += v - 1
            else:
                length += v
        return length