class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #用nums的正负来记录该索引有没有出现过1
        for i in range(len(nums)):
            if nums[abs(nums[i])] < 0:
                return abs(nums[i])
            #防止索引已经变负都要加abs
            nums[abs(nums[i])] = -nums[abs(nums[i])]