class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-1):
            #奇数
            if i % 2 and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            #偶数
            if not i % 2 and nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]