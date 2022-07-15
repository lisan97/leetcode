class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]

        [[9,5,1],
        [10,6,2],
        [11,7,3],
        [12,8,4]]
        """
        #行转列
        m = len(matrix)
        n = len(matrix[0])
        res = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][m-i-1] = matrix[i][j]
        return res
    
if __name__ == '__main__':
    matrix = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]
    print(Solution().rotate(matrix))