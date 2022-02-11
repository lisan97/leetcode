class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        '''
        状态：健康点
        选择：往下还是往右
        从 grid[i][j] 到达终点（右下角）所需的最少生命值是 dp[i][j]
        base case：dp[i][j] = -dungeon[i][j] + 1 if dungeon[i][j]<=0 else 1
        根据选择，状态转移的逻辑:dp[i][j] = min(dp[i+1][j],dp[i][j+1]) - dungeon[i][j]
        '''
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[0]*n for _ in range(m)]
        dp[m-1][n-1]= -dungeon[m-1][n-1] + 1 if dungeon[m-1][n-1]<=0 else 1
        for i in range(m-2,-1,-1):
            res = dp[i+1][n-1] - dungeon[i][n-1]
            dp[i][n-1] = res if res > 0 else 1
        for j in range(n-2,-1,-1):
            res = dp[m-1][j+1] - dungeon[m-1][j]
            dp[m-1][j] = res if res > 0 else 1
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                res = min(dp[i+1][j],dp[i][j+1]) - dungeon[i][j]
                #骑士的生命值至少为 1
                dp[i][j] = res if res > 0 else 1
        return dp[0][0]