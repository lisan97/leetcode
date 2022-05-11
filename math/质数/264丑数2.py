class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        from heapq import *
        if n == 1:
            return 1
        hq = [1]
        while n > 0:
            num = heappop(hq)
            for i in [2,3,5]:
                heappush(hq,num*i)
                if not num % i:
                    break
            n -= 1
        return num