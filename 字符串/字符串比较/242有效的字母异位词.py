class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import defaultdict
        dic = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            dic[s[i]] += 1
            dic[t[i]] -= 1
        for k in dic:
            if dic[k]:
                return False
        return True