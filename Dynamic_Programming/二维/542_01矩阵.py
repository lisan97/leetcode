class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        '''
        我们发现 dp[i][j] 是由其上下左右四个状态来决定，无法从一个方向开始递推
        于是我们尝试将问题分解：
        1.距离(i,j) 最近的 0 的位置，是在其 「左上，右上，左下，右下」4个方向之一；
        2.因此我们分别从四个角开始递推，就分别得到了位于「左上方、右上方、左下方、右下方」距离(i,j) 的最近的 0的距离，取 min即可；
        3.通过上两步思路，我们可以很容易的写出 4个双重 for循环
        优化：其实还可以优化成从任一组对角开始的 2次递推，比如只写从左上角、右下角开始递推就行了
        '''
        m = len(mat)
        n = len(mat[0])
        dp = [[float('inf')] *n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = min(dp[i][j],dp[i-1][j]+ 1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j],dp[i][j-1]+ 1)

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if mat[i][j] != 0:
                    if i < m-1:
                        dp[i][j] = min(dp[i][j],dp[i+1][j]+ 1)
                    if j < n-1:
                        dp[i][j] = min(dp[i][j],dp[i][j+1]+ 1)
        return dp