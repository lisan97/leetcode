class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #排序，然后看左边从哪里开始不一样，右边从哪里开始不一样
        if not nums:
            return 0
        def isSort(nums):
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    return False
            return True
        if isSort(nums):
            return 0
        numsort = sorted(nums)
        n = len(nums)
        left = 0
        while left <= n-1 and numsort[left] == nums[left]:
            left += 1
        right = n-1
        while right >= 0 and numsort[right] == nums[right]:
            right -= 1
        return right - left + 1

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #从左到右遍历寻找最大值，并维护right为最后一个小于最大值的索引位置
        #从右往左遍历寻找最小值，并维护left为最后一个大于最小值的索引位置
        n = len(nums)
        maxn = float('-inf')
        minn = float('inf')
        left = -1
        right = -1
        for i in range(n):
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]
            if minn < nums[n-i-1]:
                left = n-i-1
            else:
                minn = nums[n-i-1]
        return right - left + 1 if right != -1 else 0