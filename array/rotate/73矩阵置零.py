#空间复杂度O(m+n)
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row = set()
        col = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in row:
            for j in range(n):
                matrix[i][j] = 0
        for j in col:
            for i in range(m):
                matrix[i][j] = 0

#空间复杂度O(1)
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rowZero = False
        colZero = False
        for i in range(m):
            if matrix[i][0] == 0:
                colZero = True
                break

        for j in range(n):
            if matrix[0][j] == 0:
                rowZero = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if rowZero:
            for j in range(n):
                matrix[0][j] = 0

        if colZero:
            for i in range(m):
                matrix[i][0] = 0