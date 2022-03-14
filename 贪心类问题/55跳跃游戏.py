class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        res = 0
        for i in range(n):
            #当前最远距离无法到达该下标，则返回false
            if res < i:
                return False
            #每一步都计算一下从当前位置最远能够跳到哪里，然后和一个全局最优的最远位置 farthest 做对比，通过每一步的最优解，更新全局最优解，这就是贪心
            res = max(res,nums[i]+i)
        return True