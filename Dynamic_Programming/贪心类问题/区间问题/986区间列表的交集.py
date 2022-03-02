class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        m = len(firstList)
        n = len(secondList)
        i = 0
        j = 0
        while i < m and j < n:
            a1, a2 = firstList[i][0], firstList[i][1]
            b1, b2 = secondList[j][0], secondList[j][1]
            #两个区间存在交集
            if a2 >= b1 and b2 >= a1:
                res.append([max(a1,b1),min(a2,b2)])
            #指针前进
            if b2 >= a2:
                i += 1
            else:
                j += 1
        return res