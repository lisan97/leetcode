class Solution(object):
    def lengthOfLongestSubstringKDistinct(self,s,k):
        from collections import defaultdict
        window = defaultdict(int)
        n = len(s)
        left = 0
        right = 0
        max_len = 0
        while right < n:
            c = s[right]
            right += 1
            window[c] += 1
            while len(window) > k:
                d = s[left]
                left += 1
                window[d] -= 1
                if window[d] == 0:
                    del window[d]
            if right - left > max_len:
                max_len = right - left
        return max_len




if __name__ == '__main__':
    s = "eceba"
    k = 2
    print(Solution().lengthOfLongestSubstringKDistinct(s,k))