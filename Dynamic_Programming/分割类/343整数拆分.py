class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        #状态：第i个数
        #选择：拆分成2个，或多个
        #dp[i]：正整数i拆分后的最大乘积
        #base case:dp[0] = 0;dp[1]=0(1没法拆)
        #dp[i] = max(j*(i-j),j*dp[i-j])
        #设第1个数是j，如果只拆成2个，那么就是j*(i-j)，如果拆成多个，那么就是j乘上(i-j)拆分后的最大乘积
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i],j*(i-j),j*dp[i-j])
        return dp[-1]

#数学,O(1),O(1)
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        #推论一： 若拆分的数量 a 确定， 则 各拆分数字相等时 ，乘积最大。
        #推论二： 将数字 n 尽可能以因子 3 等分时，乘积最大。
        #拆分规则：
        # 最优： 3 。把数字 n 可能拆为多个因子 3 ，余数可能为 0,1,2 三种情况。
        # 次优： 2 。若余数为 2 ；则保留，不再拆为 1+1 。
        # 最差： 1 。若余数为 1 ；则应把一份 3 + 1替换为 2 + 2，因为 2×2>3×1。
        if n <= 3:
            return n-1
        a = n // 3
        b = n % 3
        if b == 0:
            return int(math.pow(3,a))
        elif b == 1:
            return int(2 * 2 * math.pow(3,a-1))
        else:
            return int(2 * math.pow(3,a))