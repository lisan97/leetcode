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

#