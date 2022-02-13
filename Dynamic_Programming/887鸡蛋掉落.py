#时间复杂度是 O(K*N^2)，会超过时间限制
class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        # 状态是鸡蛋的个数k和要搜索的楼的范围n
        # 选择：从几楼扔
        # dp(k,n)还剩k个鸡蛋，n层楼时的最小操作次数
        # base case：k=1时只能线性搜索，dp(1,n)=n；n=0时，不用再搜索，dp(k,0)=0
        # 状态转移，这次扔鸡蛋破没破：如果破了dp(k-1,i-1)；如果没破dp(k,N-i)
        # 因为只是确定最少操作次数，不需要管具体楼层，所以只需要记录还有几层楼要搜索就行
        self.memo = {}
        self.K = K
        self.N = N
        return self.dp(K, N)

    def dp(self, k, n):
        if k == 1:
            return n
        if n == 0:
            return 0
        if (k, n) in self.memo:
            return self.memo[(k, n)]
        res = float('inf')
        for i in range(1, n + 1):
            res = min(res,
                      #因为我们要求的是最坏情况下扔鸡蛋的次数，所以鸡蛋在第i层楼碎没碎，取决于那种情况的结果更大
                      max(
                          self.dp(k - 1, i - 1),  # 碎
                          self.dp(k, n - i)
                      ) + 1  # 没碎
                      )
        self.memo[(k, n)] = res
        return res

#总时间复杂度是 O(K*N*logN)
class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        self.memo = {}
        self.K = K
        self.N = N
        return self.dp(K, N)

    def dp(self, k, n):
        if k == 1:
            return n
        if n == 0:
            return 0
        if (k, n) in self.memo:
            return self.memo[(k, n)]
        # 因为dp(K - 1, i - 1)单调递增，dp(K, N - i)单调递减，可以用二分搜索代替线性搜索，搜索谷底
        left = 1
        right = n
        res = float('inf')
        while left <= right:
            mid = (left + right) // 2
            broken = self.dp(k - 1, mid - 1)
            not_broken = self.dp(k, n - mid)
            if not_broken > broken:
                left = mid + 1
                res = min(res, not_broken + 1)
            else:
                right = mid - 1
                res = min(res, broken + 1)
        self.memo[(k, n)] = res
        return self.memo[(k, n)]

#复杂度 O(KN)
class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        #当前有 k 个鸡蛋，可以尝试扔 m 次鸡蛋,这个状态下，最坏情况下最多能确切测试一栋 n 层的楼
        dp = [[0]*(N+1) for _ in range(K+1)]
        m = 0
        while dp[K][m] < N:
            m += 1
            for k in range(1,K+1):
                #总的楼层数 = 楼上的楼层数 + 楼下的楼层数 + 1（当前这层楼）,m是允许操作的上界，所以m-1
                dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1
        return m