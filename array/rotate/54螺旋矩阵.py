class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        m = len(matrix)
        n = len(matrix[0])
        upper_bound = 0
        lower_bound = m - 1
        left_bound = 0
        right_bound = n - 1
        #螺旋遍历，相应的边界会收缩
        while len(res) < m * n:
            if upper_bound <= lower_bound:
                for i in range(left_bound,right_bound+1):
                    res.append(matrix[upper_bound][i])
                upper_bound += 1
            if left_bound <= right_bound:
                for i in range(upper_bound,lower_bound+1):
                    res.append(matrix[i][right_bound])
                right_bound -= 1
            if upper_bound <= lower_bound:
                for i in range(right_bound, left_bound-1,-1):
                    res.append(matrix[lower_bound][i])
                lower_bound -= 1
            if left_bound <= right_bound:
                for i in range(lower_bound,upper_bound-1,-1):
                    res.append(matrix[i][left_bound])
                left_bound += 1
        return res