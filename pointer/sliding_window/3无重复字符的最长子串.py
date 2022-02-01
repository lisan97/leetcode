class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        window = defaultdict(int)
        left, right =0,0
        res = 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1
            #判断左侧窗口是否要收缩
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            #在收缩窗口完成后更新 res，收缩完成后一定保证窗口中没有重复
            res = max(res,right-left)
        return res
