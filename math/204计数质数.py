class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in [0,1]:
            return 0
        isPrime = [True] * n
        isPrime[0],isPrime[1] = False,False
        for i in range(2,n):
            if isPrime[i]:
                #比如 n = 25，i = 4 时算法会标记 4 × 2 = 8，4 × 3 = 12 等等数字，但是这两个数字已经被 i = 2 和 i = 3 的 2 × 4 和 3 × 4 标记了
                #所以让 j 从 i 的平方开始遍历
                for j in range(i*i,n,i):
                    isPrime[j] = False
        return sum(isPrime)