#字典，时间O(n)，空间O(n)
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1
        for n in range(1,len(nums)+1):
            if dic[n] == 2:
                dup = n
            if dic[n] == 0:
                miss = n
        return [dup,miss]

#时间O(n)，空间O(1)
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                dup = abs(nums[i])
            else:
                nums[index] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
        return [dup,missing]