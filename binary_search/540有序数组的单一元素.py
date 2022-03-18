class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res

#要求时间复杂度o(logn)，空间复杂度o(1)
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        根据题目描述，数组应该呈现为nums[0] == nums[1], nums[2] == nums[3]的形式，也就是nums[i] == nums[i^1]
        如果不相等，那么说明分割点在该点左边，导致了错位；如果相等，说明分割点在该点右边，还没有错位。
        也就是如果nums[mid] == nums[mid^1]，我们要left = mid + 1；否则我们要right = mid
        '''
        n = len(nums)
        if n == 1:
            return nums[0]
        left = 0
        right = n - 1
        while left < right:
            mid = (right-left)//2+left
            if nums[mid] == nums[mid^1]:
                left = mid + 1
            else:
                right = mid
        return nums[left]