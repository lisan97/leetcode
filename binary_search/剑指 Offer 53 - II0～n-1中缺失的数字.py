class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #二分查找
        #第一个值和下标不相等的元素->查找右边界
        left = 0
        right = len(nums)
        while left < right:
            mid = (left+right)//2
            if nums[mid] == mid: #缺失的在右侧
                left = mid + 1
            else: #缺失的在左侧
                right = mid
        return left