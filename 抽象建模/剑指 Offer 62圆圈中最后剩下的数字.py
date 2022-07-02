#递归
class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        # 要得到n个数序列最后剩下的数字，只需要找到n-1个数序列最后剩下的数字；n=1时，只有一个数字0
        # f(n,m) = (f(n-1,m)+m) % n;n=1时f(n,m)=0
        # 反推的过程，就是 (当前index + m) % 上一轮剩余数字的个数。
        import sys
        sys.setrecursionlimit(100000)
        return self.help(n, m)

    def help(self, n, m):
        if n == 1:
            return 0
        last = self.help(n - 1, m)
        return (last + m) % n

#循环,反推
class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        last = 0
        for i in range(2,n+1):
            last = (last + m) % i
        return last