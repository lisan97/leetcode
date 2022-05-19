class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            #右半段单调递增
            if nums[mid] <= nums[right]:
                #在右半段
                if target <= nums[right] and target > nums[mid]:
                    left =  mid + 1
                else:
                    #target > nums[right]和target < nums[mid]的情况
                    right = mid - 1
            #左半段单调递增
            else:
                #在左半段
                if target > nums[right] and target < nums[mid]:
                    right = mid - 1
                else:
                    #target <= nums[right]和target > nums[mid]的情况
                    left = mid + 1
        return -1