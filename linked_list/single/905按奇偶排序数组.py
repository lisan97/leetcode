class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if not n:
            return []
        i = 0
        j = n-1
        while i < j:
            #当i < j且nums[i]是偶数，不断往左移
            while i < j and not nums[i] % 2:
                i += 1
            #当i < j且nums[j]是奇数，不断往右移
            while i < j and nums[j] % 2:
                j -= 1
            #此时nums[i]为奇数，nums[j]为偶数，交换
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return nums