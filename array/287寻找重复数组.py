class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #用nums的正负来记录该索引有没有出现过1
        for i in range(len(nums)):
            pos = abs(nums[i])
            if nums[pos] < 0:
                return pos
            #防止索引已经变负都要加abs
            nums[pos] = -nums[pos]