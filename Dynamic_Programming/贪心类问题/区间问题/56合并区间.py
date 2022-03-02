class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        if n == 1:
            return intervals
        # 按区间的 start 升序排列
        intervals.sort(key=lambda x:(x[0]))
        res = [intervals[0]]
        for i in range(1,n):
            # res 中最后一个元素的引用
            last = res[-1]
            cur = intervals[i]
            if last[1] >= cur[0]:
                # 找到最大的 end
                last[1] = max(last[1],cur[1])
            else:
                # 处理下一个待合并区间
                res.append(cur)
        return res