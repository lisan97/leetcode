class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #状态：在第几号屋前
        #选择：偷or不偷
        #dp[i]代表前i家可获得的最高金额
        #base case:dp[0] = nums[0];dp[1] = max(nums[:2])
        #状态转移逻辑：dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]

#状态压缩
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #状态：在第几号屋前
        #选择：偷or不偷
        #dp[i]代表前i家可获得的最高金额
        #base case:dp[0] = nums[0];dp[1] = max(nums[:2])
        #状态转移逻辑：dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        n = len(nums)
        if n == 1:
            return nums[0]
        pre = nums[0]
        cur = max(nums[:2])
        tmp = cur
        for i in range(2,n):
            tmp = max(cur,pre+nums[i])
            pre = cur
            cur = tmp
        return cur