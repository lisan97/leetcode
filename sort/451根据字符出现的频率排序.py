class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import defaultdict
        dic = defaultdict(int)
        max_count = 0
        for c in s:
            dic[c] += 1
            max_count = max(max_count,dic[c])
        buckets = [[] for _ in range(max_count+1)]
        for k,v in dic.items():
            buckets[v].append(k)
        res = ''
        for i in range(len(buckets)-1,0,-1):
            for c in buckets[i]:
                for _ in range(i):
                    res += c
        return res