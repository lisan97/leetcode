class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return []
        import math
        num = math.pow(10,n)
        return [i for i in range(1,int(num))]