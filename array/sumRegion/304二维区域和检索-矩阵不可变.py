class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i in range(1,(len(matrix)+1)):
            for j in range(1,(len(matrix[0])+1)):
                self.matrix[i][j] = self.matrix[i][j-1] + self.matrix[i-1][j] - self.matrix[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.matrix[row2+1][col2+1] - self.matrix[row2+1][col1] - self.matrix[row1][col2+1] + self.matrix[row1][col1]
