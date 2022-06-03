#回溯，超时
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.res = 0
        self.n = len(nums)
        self.backtrack(nums,0,target)
        return self.res

    def backtrack(self,nums,index,remain):
        if index == self.n:
            #说明恰好凑出 target
            if remain == 0:
                self.res += 1
            return
        #减号
        remain += nums[index]
        self.backtrack(nums,index+1,target)
        remain -= nums[index]
        #加号
        remain -= nums[index]
        self.backtrack(nums,index+1,target)
        remain += nums[index]

#动态规划1
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #状态：index和remain
        #选择： + or -
        #dp(index,remain)在nums[index]，剩余为remain时，有多少种可能
        #base case: index == n时，看remain是否为0
        #状态转移：dp(index,remain) = dp(index+1,remain-nums[index]) + dp(index+1,remian+nums[index])
        #消除重叠子问题：memo[index+remain]记录
        self.memo = {} #备忘录
        self.n = len(nums)
        return self.dp(nums,0,target)

    def dp(self,nums,index,remain):
        #base case
        if index == self.n:
            if remain == 0:
                return 1
            return 0
        key = str(index)+','+str(remain)
        if key in self.memo:
            return self.memo[key]
        result = self.dp(nums,index+1,remain-nums[index]) + self.dp(nums,index+1,remain+nums[index])
        self.memo[key] = result
        return result

#转换为子集划分问题
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #转换为子集划分问题，把 nums 划分成两个子集 A 和 B，分别代表分配 + 的数和分配 - 的数,
        #看看能找到多少个子集A，和为(sum(nums) + target)/2
        #状态：前i个，j容量
        #选择：装 or 不装 nums[i-1]
        #dp(i,j)前i个，容量为j装满的方法有几种
        #base case:dp[0][1:]=0,dp[0][0]=1
        #状态转移：dp(i,j) = dp(i-1,j) + dp(i-1,j-nums[i-1])
        total = sum(nums)
        if total < abs(target) or (total + target) % 2 != 0:
            return 0
        t = (total + target) / 2
        n = len(nums)
        dp = [[0] * (t+1) for _ in range(n+1)]
        #base case
        dp[0][0] = 1
        #因为存在nums[i]=0的情况，所以base case不能这样设：
        # for i in range(n+1):
        #     dp[i][0] = 1
        for i in range(1,n+1):
            for j in range(t+1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

#状态压缩
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #转换为背包问题：取哪几个数加起来=(sum(nums)+target)/2
        #dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
        #base case:dp[0][1:] = 0,dp[0][0] = 1
        if not nums:
            return 0
        total = sum(nums)
        if total < abs(target) or (total+target) % 2:
            return 0
        t = (total+target) / 2
        n = len(nums)
        dp = [0]*(t+1)
        dp[0] = 1
        for i in range(1,n+1):
            for j in range(t,-1,-1):
                if j >= nums[i-1]:
                    dp[j] = dp[j] + dp[j-nums[i-1]]
        return dp[-1]

if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    target = 3
    #5
    print(Solution.findTargetSumWays(nums, target))