class Solution(object):
    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        '''
        等式左边必为偶数,那就让A[i]和A[j]一个为奇数一个为偶数即可
        如果一个数组是漂亮数组，那么其线性变换之后的数组也是漂亮数组，即如果[x1, x2, x3]是一个漂亮数组，
        则[k * x1 + b, k * x2 + b, k * x3 + b] 也一定是漂亮数组。这是本题能用分治思想的核心所在
        对于 left 部分，我们进行 k = 1/2, b = 1/2 的仿射变换，把这些奇数一一映射到不超过 (N + 1) / 2 的整数。
        对于 right 部分，我们进行 k = 1/2, b = 0 的仿射变换，把这些偶数一一映射到不超过 N / 2 的整数。
        经过映射，left 和 right 部分变成了和原问题一样，但规模减少一半的子问题，这样就可以使用分治算法解决了。
        '''
        self.memo = {1:[1]}
        return self.dp(n)

    def dp(self,n):
        if n not in self.memo:
            self.memo[n] = [2*i - 1 for i in self.dp((n+1)//2)] + [2*j for j in self.dp(n//2)]
        return self.memo[n]