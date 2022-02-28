class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        #状态有三个：开始的索引 i，结束的索引 j，当前轮到的人
        #选择有两个：选择最左边的那堆石头，或者选择最右边的那堆石头
        #dp[i][j][0]在(i,j)石堆间，先手能拿到的最高分
        #dp[i][j][1]在(i,j)石堆间，后手能拿到的最高分
        #dp[i][j][0] = max(piles[i]+dp[i+1][j][1],piles[j]+dp[i][j-1])
        n = len(piles)
        dp = [[[0]*2 for _ in range(n)] for _ in range(n)]
        #base case：只有一堆石头
        for i in range(n):
            dp[i][i][0] = piles[i]
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                # 解释：我作为先手，面对 piles[i...j] 时，有两种选择：
                # 要么我选择最左边的那一堆石头，然后面对 piles[i+1...j]
                # 但是此时轮到对方，相当于我变成了后手；
                # 要么我选择最右边的那一堆石头，然后面对 piles[i...j-1]
                # 但是此时轮到对方，相当于我变成了后手。
                # 解释：我作为后手，要等先手先选择，有两种情况：
                # 如果先手选择了最左边那堆，给我剩下了 piles[i+1...j]
                # 此时轮到我，我变成了先手；
                # 如果先手选择了最右边那堆，给我剩下了 piles[i...j-1]
                # 此时轮到我，我变成了先手。
                left = piles[i] + dp[i+1][j][1]
                right = piles[j] + dp[i][j-1][1]
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i+1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j-1][0]
        return dp[0][n-1][0] - dp[0][n-1][1] > 0

#先手的其实肯定赢
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        #作为第一个拿石头的人，你可以控制自己拿到所有偶数堆，或者所有的奇数堆，
        # 可以在第一步就观察好，奇数堆的石头总数多，还是偶数堆的石头总数多，然后步步为营，就一切尽在掌控之中了
        return True