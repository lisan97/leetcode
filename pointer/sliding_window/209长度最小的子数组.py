class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        j = 0
        min_len = float('inf')
        cur = 0
        while j < n:
            cur += nums[j]
            j += 1
            while cur >= target:
                length = j - i
                min_len = min(length,min_len)
                cur -= nums[i]
                i += 1
        return 0 if min_len == float('inf') else min_len