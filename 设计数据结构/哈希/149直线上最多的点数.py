class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        dic = defaultdict(set)
        if len(points) == 1:
            return 1
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                if points[i][0] == points[j][0]:
                    slope = 2e4+1
                    bias = points[i][0]
                else:
                    slope = float(points[i][1]-points[j][1]) / float(points[i][0]-points[j][0])
                    bias = float(points[i][1]) - points[i][0] * slope
                dic[(slope,bias)].add((points[i][0],points[i][1]))
                dic[(slope,bias)].add((points[j][0],points[j][1]))
        res = 0
        for k in dic:
            res = max(res,len(dic[k]))
        return res