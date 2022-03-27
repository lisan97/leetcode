#递归
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        #「备忘录」数组或字典
        self.memo = [0] * (n+1)
        return self.helper(n)
    def helper(self,n):
        if n in [0,1]:
            return n
        if self.memo[n] != 0:
            return self.memo[n]
        self.memo[n] = self.helper(n-1) + self.helper(n-2)
        return self.memo[n]

#迭代
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        #DP table
        dp = [0] * (n+1)
        #base case
        dp[0] = 0
        dp[1] = 1
        #状态转移
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

#状态压缩
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        pre, cur = 0, 1
        for _ in range(2,n+1):
            sum = pre + cur
            pre = cur
            cur = sum
        return cur