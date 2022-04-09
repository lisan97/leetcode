class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #首先我们考虑一个数字是不是 2 的（整数）次方,如果 n & (n - 1) 为 0，那么这个数是 2 的次方
        #如果这个数也是 4 的次方，那二进制表示中 1 的位置必须为奇数位。我们可以把 n 和二进制的 10101...101（即十进制下的 1431655765）做按位与，如果结果不为 0，那么说明这个数是 4 的次方
        if n <= 4:
            if n in [1,4]:
                return True
            return False
        n = n ** 0.5
        if n % 1:
            return False
        n = int(n)
        return n&(n-1) == 0

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #首先我们考虑一个数字是不是 2 的（整数）次方,如果 n & (n - 1) 为 0，那么这个数是 2 的次方
        #如果这个数也是 4 的次方，那二进制表示中 1 的位置必须为奇数位。我们可以把 n 和二进制的 10101...101（即十进制下的 1431655765）做按位与，如果结果不为 0，那么说明这个数是 4 的次方
        return n > 0 and not n&(n-1) and (n & 1431655765) != 0