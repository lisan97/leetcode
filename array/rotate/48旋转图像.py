class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 先沿对角线镜像对称二维矩阵
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 然后反转二维矩阵的每一行
        for i in range(len(matrix)):
            self.reverse(matrix[i])
        return matrix

    def reverse(self, row):
        i = 0
        j = len(row) - 1
        while j > i:
            row[i], row[j] = row[j], row[i]
            i += 1
            j -= 1