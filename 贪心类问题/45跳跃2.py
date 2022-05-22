#动态规划
#递归深度 × 每次递归需要的时间复杂度，即 O(N^2)
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #状态：在哪个位置
        #选择：跳几格
        #dp[i]从i到最后一格的最少次数
        #base case:dp[-1]=0
        #状态转移：dp[i] = min(dp[i+1]...dp[i+nums[i]])+1
        n = len(nums)
        dp = [n] * n
        dp[-1] = 0
        for i in range(n-2,-1,-1):
            for j in range(nums[i]):
                j += 1
                if i+j>n-1:
                    continue
                dp[i] = min(dp[i],dp[i+j]+1)
        return dp[0]

#贪心
#时间O(N);空间O(1)
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #每一跳选下一个位置能跳到最远的位置
        farthest = 0 #farthest 标记了所有选择 [i..end] 中能够跳到的最远距离
        end = 0 #i 和 end 标记了可以选择的跳跃步数
        count = 0
        for i in range(len(nums)-1):
            farthest = max(nums[i]+i,farthest)
            if end == i:
                count += 1
                end = farthest
        return count
