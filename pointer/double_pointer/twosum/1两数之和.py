class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        #构造一个哈希表：元素映射到相应的索引
        #碰到重复的都会存后一个索引
        for i in range(len(nums)):
            dic[nums[i]] = i
        for i in range(len(nums)):
            other = target - nums[i]
            #如果 other 存在且不是 nums[i] 本身
            if other in dic and dic[other] != i:
                return [i,dic[other]]