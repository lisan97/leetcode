class Solution(object):
    def twoEggDrop(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 状态：鸡蛋个数，楼层数
        # 选择：从哪层楼扔
        # dp(k,n)代表有k个鸡蛋，检查n层楼的最小操作次数
        # base case:dp(1,n) = n;dp(k,0) = 0
        # 状态转移:dp(k,n) = max(dp(k-1,i-1),dp(k,n-i))#破了与没破里取更大的那种
        self.memo = {}
        k = 2
        return self.dp(k, n)

    def dp(self, k, n):
        if n == 0:
            return 0
        if k == 1:
            return n
        if (k, n) in self.memo:
            return self.memo[(k, n)]
        res = float('inf')
        for i in range(1, n + 1):
            res = min(res, max(self.dp(k - 1, i - 1), self.dp(k, n - i)) + 1)
        self.memo[(k, n)] = res
        return res


class Solution(object):
    def twoEggDrop(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 状态：鸡蛋个数，楼层数
        # 选择：从哪层楼扔
        # dp(k,n)代表有k个鸡蛋，检查n层楼的最小操作次数
        # base case:dp(1,n) = n;dp(k,0) = 0
        # 状态转移:dp(k,n) = max(dp(k-1,i-1),dp(k,n-i))#破了与没破里取更大的那种
        self.memo = {}
        k = 2
        return self.dp(k, n)

    def dp(self, k, n):
        if n == 0:
            return 0
        if k == 1:
            return n
        if (k, n) in self.memo:
            return self.memo[(k, n)]
        # 二分查找两个函数dp(k-1,i-1),dp(k,n-i)的交点，因为一个单调递增一个单调递减，交点处最大值的最小值最小
        left = 1
        right = n
        res = float('inf')
        while left <= right:
            mid = (left + right) // 2
            broken = self.dp(k - 1, mid - 1)
            not_broken = self.dp(k, n - mid)
            if broken == not_broken:
                res = broken + 1
                break
            if broken < not_broken:
                left = mid + 1
                res = min(res, not_broken + 1)
            else:
                right = mid - 1
                res = min(res, broken + 1)
        self.memo[(k, n)] = res
        return res