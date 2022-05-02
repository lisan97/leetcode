class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.pow(x, -n)
        else:
            return self.pow(x, n)

    def pow(self, x, n):
        '''
        n > 0
        '''
        if n == 0:
            return 1
        if n % 2:
            return x * self.pow(x, n - 1)
        else:
            sub = self.pow(x, n / 2)
            return sub * sub