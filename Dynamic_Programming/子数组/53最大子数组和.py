class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #以 nums[i] 为结尾的「最大子数组和」为 dp[i]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            #dp[i] 有两种「选择」，要么与前面的相邻子数组连接，形成一个和更大的子数组；要么不与前面的子数组连接，自成一派，自己作为一个子数组。
            dp[i] = max(dp[i-1]+nums[i],nums[i])
        return max(dp)

#状态压缩
#dp[i+1]只与dp[i]相关，因此可以进行状态压缩
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp_0 = nums[0]
        dp_1 = 0
        res = dp_0
        for i in range(1,len(nums)):
            dp_1 = max(nums[i],dp_0+nums[i])
            dp_0 = dp_1
            res = max(res,dp_0)
        return res

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    #6
    print(Solution().maxSubArray(nums))