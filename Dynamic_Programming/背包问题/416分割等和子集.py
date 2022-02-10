class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 == 1:
            return False
        #可装载重量为 sum / 2 的背包和 N 个物品
        target = sum(nums) / 2
        n = len(nums)
        #dp[i][j] = x 表示，对于前 i 个物品，当前背包的容量为 j 时，是否有一种方法把背包恰好装满
        dp = [[False]*(target+1) for _ in range(n+1)]
        #base case 就是 dp[..][0] = true 和 dp[0][..] = false，因为背包没有空间的时候，就相当于装满了，而当没有物品可选择的时候，肯定没办法装满背包
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1,n+1):
            for w in range(1,target+1):
                if w < nums[i-1]:
                    dp[i][w] = dp[i-1][w]
                else:
                    #不把这第 i 个物品装入背包,取决于上一个状态 dp[i-1][j]
                    #把这第 i 个物品装入了背包,取决于状态 dp[i-1][j-nums[i-1]]
                    dp[i][w] = dp[i-1][w-nums[i-1]] or dp[i-1][w]
        return dp[-1][-1]

#降维
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) / 2
        n = len(nums)
        #注意到 dp[i][j] 都是通过上一行 dp[i-1][..] 转移过来的，因此可以降维
        dp = [False]*(target+1)
        dp[0] = True
        for i in range(n):
            #唯一需要注意的是 j 应该从后往前反向遍历，因为每个物品（或者说数字）只能用一次，以免之前的结果影响其他的结果。
            for w in range(target,-1,-1):
                if w >= nums[i]:
                    dp[w] = dp[w] or dp[w-nums[i]]
        return dp[-1]