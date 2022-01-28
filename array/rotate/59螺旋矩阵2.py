class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0]*n for _ in range(n)]
        upper_bound = 0
        lower_bound = n-1
        left_bound = 0
        right_bound = n -1
        num = 1
        while num <= n**2:
            if upper_bound <= lower_bound:
                for i in range(left_bound,right_bound+1):
                    matrix[upper_bound][i] = num
                    num += 1
                upper_bound += 1
            if left_bound <= right_bound:
                for i in range(upper_bound,lower_bound+1):
                    matrix[i][right_bound] = num
                    num += 1
                right_bound -= 1
            if upper_bound <= lower_bound:
                for i in range(right_bound,left_bound-1,-1):
                    matrix[lower_bound][i] = num
                    num += 1
                lower_bound -= 1
            if left_bound <= right_bound:
                for i in range(lower_bound,upper_bound-1,-1):
                    matrix[i][left_bound] = num
                    num += 1
                left_bound += 1
        return matrix
