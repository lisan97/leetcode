class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #i维护偶数索引
        #j维护奇数索引
        n = len(nums)
        j = 1
        for i in range(0,n,2):
            #当遇到奇数
            if nums[i] % 2 == 1:
                #直到遇到偶数
                while nums[j] % 2 == 1:
                    j += 2
                #交换
                nums[i], nums[j] = nums[j], nums[i]
        return nums