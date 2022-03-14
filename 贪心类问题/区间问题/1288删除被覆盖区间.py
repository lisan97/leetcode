class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        #那么我们可以先算一算，被覆盖区间有多少个，然后和总数相减就是剩余区间数。
        n = len(intervals)
        if n == 1:
            return 1
        #按照起点升序排列，起点相同时降序排列
        intervals.sort(key=lambda x:(x[0],-x[1]))
        end = intervals[0][1]
        delete = 0
        for i in range(1,n):
            #找到覆盖区间
            if intervals[i][1] <= end:
                delete += 1
            #更新终点
            else:
                end = intervals[i][1]
        return n - delete