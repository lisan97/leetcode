class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #1.对于任意数组而言，一定存在峰值(对于所有有效的 i 都有 nums[i] != nums[i + 1])
        #基于1，如果当前位置大于其左边界或者右边界，那么在当前位置的右边或左边必然存在峰值。
        #假设当前分割点 mid 满足关系 num[mid] > nums[mid + 1] 的话，
        #一个很简单的想法是 num[mid] 可能为峰值，而 nums[mid + 1] 必然不为峰值，
        #于是让 r = mid，从左半部分继续找峰值。
        n = len(nums)
        if n == 1:
            return 0
        left = 0
        right = n - 1
        while left < right:
            mid = (left+right) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left