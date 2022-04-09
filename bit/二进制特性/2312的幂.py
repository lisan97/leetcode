class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #一个数如果是 2 的指数，那么它的二进制表示一定只含有一个 1
        if n <= 0:
            return False
        return (n & (n-1)) == 0