class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 3 == 0:
            n = n / 3
        return n == 1

#log,python部分用例会报错
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        return math.log(n,3) % 1 == 0