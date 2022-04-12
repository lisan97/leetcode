class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        '''
        将二维数组nums映射成一个一维数组；
        将这个一维数组映射回 r 行 c 列的二维数组。
        我们也可以直接从二维数组nums 得到 r 行 c 列的重塑矩阵：nums[i//c][i%c] = nums[i//n][i%n]
        '''
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c:
            return mat
        newMat = [[0]*c for _ in range(r)]
        for i in range(m*n):
            newMat[i//c][i%c] = mat[i//n][i%n]
        return newMat