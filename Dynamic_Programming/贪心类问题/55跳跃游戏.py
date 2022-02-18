class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        res = 0
        for i in range(n):
            #当前最远距离无法到达该下标，则返回false
            if res < i:
                return False
            res = max(res,nums[i]+i)
        return True