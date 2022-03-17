class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            mid = (right-left)//2 + left
            #当 nums[mid] > nums[right]时，midmid 一定在第 1 个排序数组中，ii 一定满足 mid < i <= right，因此执行 left = mid + 1
            if nums[mid] > nums[right]:
                left = mid + 1
            #当 nums[mid] < nums[right] 时，midmid 一定在第 2 个排序数组中，ii 一定满足 left < i <= mid，因此执行 right = mid
            elif nums[mid] < nums[right]:
                right = mid
            #当 nums[mid] == nums[right] 时,难以判断分界点 ii 指针区间,采用 right = right - 1
            else:
                right -= 1
        return nums[left]