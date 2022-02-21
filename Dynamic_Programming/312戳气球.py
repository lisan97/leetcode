class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #状态：气球区间(i,j)
        #选择：戳哪个
        #dp[i][j]表示(i,j)内的最大值
        #base case，j<=i+1无球可戳，dp[i][j] = 0
        #状态转移：关键在于dp数组的定义，需要避免子问题互相影响，所以我们反向思考,最后戳哪个球得分最高
        n = len(nums)
        #添加两侧的虚拟气球,因此(i,j)是开区间
        points = [1]*(n+2)
        for i in range(1,n+1):
            points[i] = nums[i-1]
        dp = [[0]*(n+2) for _ in range(n+2)]
        #dp[i][j]所依赖的状态是dp[i][k]和dp[k][j]，因此从下往上遍历
        for i in range(n,-1,-1):
            for j in range(i+1,n+2):
                #最后戳破的气球是哪个？
                for k in range(i+1,j):
                    dp[i][j] = max(dp[i][j],dp[i][k]+dp[k][j]+points[i]*points[k]*points[j])
        return dp[0][n+1]