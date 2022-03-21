#计数排序
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        from collections import defaultdict
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        i = 0
        for v in [0,1,2]:
            for _ in range(dic[v]):
                nums[i] = v
                i += 1

#follow up一次遍历完成