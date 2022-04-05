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

#自上而下分治
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        由于戳气球的操作，发现这会导致两个气球从不相邻变成相邻，使得后续操作难以处理；
        所以反过来看，每次从原数组内取一个气球加入1..1
        '''
        self.memo = {}
        n = len(nums)
        nums = [1] + nums + [1]
        return self.dp(0, n + 1, nums)

    def dp(self, left, right, nums):
        if (left, right) in self.memo:
            return self.memo[(left, right)]
        if left >= right - 1:
            return 0
        best = 0
        for i in range(left + 1, right):
            total = nums[i] * nums[left] * nums[right] + self.dp(left, i, nums) + self.dp(i, right, nums)
            best = max(total, best)
        self.memo[(left, right)] = best
        return best