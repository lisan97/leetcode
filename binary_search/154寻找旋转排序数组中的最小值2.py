class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        不能以nums[left]进行比较：当最小值是nums[left]时，nums[mid]>nums[left]，会误以为此时mid在第一个排序数组，将left指针右移至mid+1
        用nums[right]比较，当最小值是nums[right]时，nums[mid] > nums[right]，将left右移至mid+1，不会错过right这个点
        '''
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            mid = (right-left)//2 + left
            #当 nums[mid] > nums[right]时，mid 一定在第 1 个排序数组中，i 一定满足 mid < i <= right，因此执行 left = mid + 1
            if nums[mid] > nums[right]:
                left = mid + 1
            #当 nums[mid] < nums[right] 时，mid 一定在第 2 个排序数组中，i 一定满足 left < i <= mid，因此执行 right = mid
            elif nums[mid] < nums[right]:
                right = mid
            #当 nums[mid] == nums[right] 时,难以判断分界点 i 指针区间,采用 right = right - 1
            else:
                right -= 1
        return nums[left]