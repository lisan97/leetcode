#O(n),O(1)
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #直接在原数组上，将出现过的(数字-1)索引的数设为负数
        #然后再遍历一遍，返回数组中仍为正数的(索引+1)
        res = []
        for num in nums:
            pos = abs(num) - 1#防止出现多次，已经该数为负的情况
            if nums[pos] > 0:
                nums[pos] = - nums[pos]
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res