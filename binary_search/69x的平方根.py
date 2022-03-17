class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x // 2 + 1
        while left <= right:
            mid = (right-left)//2 + left
            sqrt = mid ** 2
            if sqrt == x:
                return mid
            elif sqrt < x:
                left = mid + 1
            else:
                right = mid - 1
        return left-1
#也可以用除法