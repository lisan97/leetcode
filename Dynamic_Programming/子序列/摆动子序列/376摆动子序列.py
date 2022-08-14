class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #状态：i,负号(0)or正号(1)
        #dp[i][j]截止到i为止以负号或者正号结尾摆动序列的最长子序列长度
        #base case:dp[0][0],dp[0][1]=1, 如果nums[0]!=nums[1] dp[1][0],dp[1][1] = 2，否则dp[1][0],dp[1][1] = 1
        #状态转移: i循环和前i-1个数做差,如果为负，max(dp[i][0],dp[j][1] + 1);如果为正max(dp[i][1],dp[j][0] + 1);如果为0,dp[i][:] = dp[j][:]
        n = len(nums)
        if n == 1:
            return 1
        dp = [[1]*2 for _ in range(n)]
        for i in range(1,n):
            num = nums[i]
            for j in range(i):
                diff = num - nums[j]
                if diff > 0:
                    dp[i][1] = max(dp[i][1],dp[j][0] + 1)
                elif diff < 0:
                    dp[i][0] = max(dp[i][0],dp[j][1] + 1)
                else:
                    dp[i][0] = max(dp[i][0],dp[j][0])
                    dp[i][1] = max(dp[i][1],dp[j][1])
        return max(dp[-1])

#贪心,时间O(n),空间O(1)
class Solution:
    def wiggleMaxLength(self, nums):
        n = len(nums)
        if n < 2:
            return n
        up = 1
        down = 1
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                #up[i] = down[i - 1] + 1
                #down[i] = down[i - 1]
                up = down + 1
            elif nums[i] < nums[i-1]:
                #up[i] = up[i - 1]
                #down[i] = up[i - 1] + 1
                down = up + 1
            # else:
            #     up[i] = up[i - 1]
            #     down[i] = down[i - 1]
        return max(up,down)