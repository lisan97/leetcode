class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 1:
            return 1
        points.sort(key=lambda x:x[1])
        #至少有一个区间不相交
        count = 1
        #排序后，第一个区间就是 x
        end = points[0][1]
        for point in points[1:]:
            start = point[0]
            if start > end:
                #找到下一个选择的区间了
                count += 1
                end = point[1]
        return count