class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 1:
            return 0
        intervals.sort(key=lambda x:x[1])
        count = 0
        end = intervals[0][1]
        for interval in intervals[1:]:
            start = interval[0]
            if start < end:
                count += 1
            else:
                end = interval[1]
        return count
#逆向思维
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n = len(intervals)
        if n == 1:
            return 0
        intervals.sort(key=lambda x:x[1])
        count = 1
        end = intervals[0][1]
        for interval in intervals[1:]:
            start = interval[0]
            if start >= end:
                count += 1
                end = interval[1]
        #求出最大不相交子集，剩下的就是相交要剔除的数量
        return n - count