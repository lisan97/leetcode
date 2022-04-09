#O(nlogn)
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [self.countOnes(i) for i in range(n+1)]

    def countOnes(self,num):
        count = 0
        while num:
            num &= (num-1)
            count += 1
        return count

#O(n)动态规划
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        #状态i
        #dp[i]整数i的1的个数
        #base case:dp[0] = 0
        #状态转移:dp[i] = dp[i&(i-1)] + 1
        dp = [0] * (n+1)
        for i in range(1,n+1):
            dp[i] = dp[i&(i-1)] + 1
        return dp