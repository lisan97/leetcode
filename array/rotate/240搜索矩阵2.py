class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #可以从(0,n-1)这个点开始搜索,因为它是该行最大的值，该列最小的值
        #i=0,j=n-1
        #若target > matrix[i][j] i += 1;
        #若target < matrix[i][j] j-= 1
        #若i = m 或j=-1说明没找到
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n-1
        while i < m and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                j -= 1
            else:
                i += 1
        return False