class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #先用dic统计每个数出现的索引
        from collections import defaultdict
        dic = defaultdict(list)
        n = len(nums)
        for i in range(n):
            dic[nums[i]].append(i)
        max_degree = 1
        min_length = 1
        #然后根据频率和第一个与最后一个索引的跨度，对拥有最大度的最短连续子数组的长度进行更新
        for k,v in dic.items():
            degree = len(v)
            if degree == max_degree:
                min_length = min(min_length,v[-1] - v[0]+1)
            elif degree > max_degree:
                max_degree = degree
                min_length = v[-1] - v[0]+1
            else:
                continue
        return min_length