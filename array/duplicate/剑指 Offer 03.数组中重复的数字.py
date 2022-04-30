#下标当哈希表，取负，再遇到负数就是第一个重复的数
#对0需特殊规则
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zero_num = 0
        for num in nums:
            pos = abs(num)
            if nums[pos] == 0:
                if zero_num == 1:
                    return 0
                zero_num += 1
            elif nums[pos] < 0:
                return pos
            else:
                nums[pos] = -nums[pos]
        return -1

#原地修改
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        #因为是0~n-1，如果都不重复，可以指标与数值一一对应
        for i,val in enumerate(nums):
            if val < 0 or val > len(nums) - 1:
                return -1
            while i != val:
                #如果nums[i] == nums[val]，则找到了重复项
                if val == nums[val]:
                    return val
                #不断进行交换，直到nums[i] == i
                nums[i], nums[val] = nums[val], nums[i]
                val = nums[i] #更新val
        return -1