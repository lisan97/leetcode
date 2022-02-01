class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import defaultdict
        need,window = defaultdict(int), defaultdict(int)
        left,right = 0,0
        valid = 0
        start = 0
        for c in p:
            need[c] += 1
        res = []
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
                if valid == len(need):
                    res.append(left)
            while right - left >= len(p):
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res