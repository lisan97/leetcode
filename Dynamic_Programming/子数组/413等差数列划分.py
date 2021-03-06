class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #子数组的dp定义是：以nums[i]结尾的等差数列的个数
        #base case:dp[0]=0,dp[1]=0
        #状态转移：dp[i] = dp[i-1] + 1
        n = len(nums)
        if n < 3:
            return 0
        dp = [0] * n
        for i in range(2,n):
            #子数组必定满足 num[i] - num[i-1] = num[i-1] - num[i-2]
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
        #等差子数组可以在任意一个位置终结，在最后需要对 dp 数组求和
        return sum(dp)