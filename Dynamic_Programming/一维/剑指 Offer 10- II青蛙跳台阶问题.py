class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n in [1,2]:
            return n
        pre_2 = 1
        pre_1 = 2
        cur = 0
        for _ in range(3,n+1):
            cur = pre_1 + pre_2
            pre_2 = pre_1
            pre_1 = cur
        return cur % 1000000007