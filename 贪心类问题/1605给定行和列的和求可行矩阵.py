class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        #将第i行第jj列设为min(row[i],col[j])，同时更新row[i]和col[j]即可
        '''
        其实很简单。我们首先考虑第一行，显然有row[0]≤∑col[j]，
        因此在经过上述操作后，一定能使得row[0]=0。
        同时，因为每次我们取得是min(row[0],col[j])，所以操作后，一定仍满足∀j,col[j]≥0。
        这样，我们就把原问题变成了N-1行，M列的新问题。依次类推，我们就一定能够得到一组可行解。
        '''
        m = len(rowSum)
        n = len(colSum)
        matrix = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                matrix[i][j] = min(rowSum[i],colSum[j])
                rowSum[i] -= matrix[i][j]
                colSum[j] -= matrix[i][j]
        return matrix