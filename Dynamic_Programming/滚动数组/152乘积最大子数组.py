class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        i截止第i个，0代表正的最大乘积,1代表负的最小乘积
        dp[i][0/1]
        选择：当前值为正时乘以前面正的最大乘积，当前值为负时乘以负的最小乘积，为0时，都置为0
        状态转移:
        if nums[i] > 0 dp[i][0] = dp[i-1][0] * nums[i], nums[i] ; dp[i][1] = dp[i-1][1] * nums[i]
        if nums[i] < 0 dp[i][0] = dp[i-1][1] * nums[i] ; dp[i][1] = dp[i-1][0] * nums[i]
        if nums[i] == 0 dp[i][0] = 0; dp[i][1] = 0
        '''
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [[0]*2 for _ in range(n)]
        max_res = nums[0]
        if nums[0] > 0:
            dp[0][0] = nums[0]
            dp[0][1] = 0
        else:
            dp[0][0] = 0
            dp[0][1] = nums[0]
        for i in range(1,n):
            if nums[i] > 0:
                dp[i][0] = max(dp[i-1][0] * nums[i],nums[i])
                dp[i][1] = dp[i-1][1] * nums[i]
            elif nums[i] < 0:
                dp[i][0] = dp[i-1][1] * nums[i]
                dp[i][1] = min(dp[i-1][0] * nums[i],nums[i])
            else:
                dp[i][0] = 0
                dp[i][1] = 0
            max_res = max(dp[i][0],max_res)
        return max_res

#状态压缩
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        max_res = nums[0]
        if nums[0] > 0:
            dp_max = nums[0]
            dp_min = 0
        else:
            dp_max = 0
            dp_min = nums[0]
        for i in range(1,n):
            if nums[i] > 0:
                dp_max = max(dp_max * nums[i],nums[i])
                dp_min = dp_min * nums[i]
            elif nums[i] < 0:
                tmp = dp_max
                dp_max = dp_min * nums[i]
                dp_min = min(tmp * nums[i],nums[i])
            else:
                dp_max = 0
                dp_min = 0
            max_res = max(dp_max,max_res)
        return max_res