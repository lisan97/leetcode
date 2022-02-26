class Solution(object):
    def preimageSizeFZF(self, k):
        """
        :type k: int
        :rtype: int
        """
        #因为阶乘是递增的，所以可以用二分法去查找左右边界
        import sys
        left = 0
        right = sys.maxsize
        while left < right:
            mid = left + (right-left) // 2
            res = self.trailingZeroes(mid)
            if res < k:
                left = mid + 1
            else:
                right = mid
        left_side = left
        left = 0
        right = sys.maxsize
        while left < right:
            mid = left + (right-left) // 2
            res = self.trailingZeroes(mid)
            if res > k:
                right = mid
            else:
                left = mid + 1
        right_side = left-1
        return right_side - left_side + 1

    def trailingZeroes(self, n):
        res = 0
        d = n
        while d // 5 > 0:
            res += d // 5
            d = d// 5
        return res