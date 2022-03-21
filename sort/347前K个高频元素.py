class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        dic = [x[0] for x in sorted(dic.items(),key=lambda x:x[1],reverse=True)[:k]]
        return dic

#桶排序，时间复杂度O(n)，空间复杂度O(n)
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict
        dic = defaultdict(int)
        n = len(nums)
        #使用字典，统计每个元素出现的次数
        for num in nums:
            dic[num] += 1
        #将频率作为数组下标，对于出现频率不同的数字集合，存入对应的数组下标
        buckets = [[] for _ in range(n+1)]
        for i,v in dic.items():
            buckets[v].append(i)
        #倒序遍历数组获取出现顺序从大到小的排列
        res = []
        for i in range(len(buckets)-1,-1,-1):
            if len(res) == k:
                break
            res.extend(buckets[i])
        return res[:k]