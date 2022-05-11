class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        #使用优先队列，每次pop出来的那个数和所有质数乘一遍pq
        from heapq import *
        import sys
        if n == 1:
            return 1
        pq = [1]
        while n > 0:
            num = heappop(pq)
            for prime in primes:
                if prime <= sys.maxsize / num:
                    heappush(pq,num*prime)
                #使得只出现a×b,b×a不会出现(a>b)例如:7×2，2×7
                if num % prime==0:
                    break
            n -= 1
        return num