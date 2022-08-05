class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import bisect
        n = len(nums)
        res = [0] * n
        stack = []
        for i in range(n-1,-1,-1):
            index = bisect.bisect_left(stack,nums[i])
            res[i] = index
            bisect.insort(stack,nums[i])
        return res