class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        from collections import defaultdict
        need,window = defaultdict(int),defaultdict(int)
        left, right = 0,0
        valid = 0
        for c in s1:
            need[c] += 1
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
                if valid == len(need):
                    return True
            #移动 left 缩小窗口的时机是窗口大小大于len(s1)时
            while (right - left) >= len(s1):
                d = s2[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False