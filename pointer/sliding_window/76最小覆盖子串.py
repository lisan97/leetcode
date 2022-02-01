class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import defaultdict
        #需要凑齐的字符和记录窗口中的字符
        need, window = defaultdict(int),defaultdict(int)
        #区间 [left, right) 是左闭右开的
        left,right = 0,0
        #记录最小覆盖子串的起始索引及长度
        start, length = 0, float('inf')
        #表示窗口中满足 need 条件的字符个数
        valid = 0
        for c in t:
            need[c] += 1
        while right < len(s):
            c = s[right]
            right += 1
            #进行窗口内数据的一系列更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            #判断左侧窗口是否要收缩
            while valid == len(need):
                #在这里更新最小覆盖子串
                if right - left < length:
                    start = left
                    length = right - left
                #d 是将移出窗口的字符
                d = s[left]
                left += 1
                #进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return s[start:start+length] if length != float('inf') else ""