class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        dic = defaultdict(int)
        n = len(nums)
        for i in range(n):
            dic[nums[i]] += 1
        max_length = 0
        for k,v in dic.items():
            pre = k -1
            if pre in dic:
                max_length = max(max_length,v+dic[pre])
        return max_length