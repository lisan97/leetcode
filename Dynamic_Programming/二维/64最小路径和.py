class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        状态：路径数字和
        选择：往下还是往右
        dp[i][j]代表从左上角到(i,j)的最小路径和
        base case：dp[0][0]=grid[0][0]
        根据选择，状态转移的逻辑:dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]，需注意左边第一列和上面第一行的特殊情况
        '''
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*(n) for _ in range(m)]
        dp[0][0] = grid[0][0]
        #无法从左侧得到
        for i in range(1,m):
            dp[i][0] = grid[i][0]+dp[i-1][0]
        #无法从上得到
        for i in range(1,n):
            dp[0][i] = grid[0][i]+dp[0][i-1]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]

#状态压缩
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        因为 dp 矩阵的每一个值只和左边和上面的值相关，我们可以使用空间压缩将 dp 数组压缩为一维。
        对于第 i 行，在遍历到第 j 列的时候，因为第 j-1 列已经更新过了，所以 dp[j-1] 代表 dp[i][j-1]的值；
        而 dp[j] 待更新，当前存储的值是在第 i-1 行的时候计算的，所以代表 dp[i-1][j] 的值
        '''
        m = len(grid)
        n = len(grid[0])
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = grid[0][0]
                elif i == 0:
                    dp[j] = dp[j-1]+grid[i][j]
                elif j == 0:
                    dp[j] = dp[j]+grid[i][j]
                else:
                    dp[j] = min(dp[j],dp[j-1]) + grid[i][j]
        return dp[-1]