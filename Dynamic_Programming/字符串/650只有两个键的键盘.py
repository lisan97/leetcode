class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        #状态：字符A的个数
        #选择：copy or paste
        #dp[i]字符A为i个时的最少操作次数
        #base case:dp[0]=0,dp[1]=0
        #状态转移:如果 n 是素数的话，我们只能通过复制 1 次A，然后粘贴 n - 1 次的方式才能得到 n 个A。总的操作了 n 次。
        #我们必须首先拥有 j 个A，使用一次「复制全部」操作，再使用若干次「粘贴」操作得到 i 个 A
        # dp[i] = dp[j] + dp[i//j] dp[j]代表到达j个A的操作次数,dp[i//j]长度 i 由长度 j 操作得到，其操作次数等价于把一个长度为 1的 A 延展到长度为 i/j(复制1次然后粘贴i/j-1次)
        if n == 1:
            return 0
        dp = [0]*(n+1)
        for i in range(2,n+1):
            dp[i] = i
            j = 2
            while j ** 2 <= i:
                if i % j == 0:
                    dp[i] = dp[j] + dp[i//j]
                    break
                j += 1
        return dp[-1]