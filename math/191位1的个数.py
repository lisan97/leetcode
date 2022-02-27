class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #一个循环不停地消除 1 同时计数，直到 n 变成 0 为止
        res = 0
        while n != 0:
            n = n & (n-1)
            res += 1
        return res