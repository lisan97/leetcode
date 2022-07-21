'''
输入一个浮点数，输出平方根，要求保留精度
'''
class Solution(object):
    def mySqrt(self, x,p):
        """
        :type x: float
        :type p: float
        :rtype: float
        """
        left = 0
        right = x
        while left <= right:
            mid = (left+right)/2.0
            sqrt = mid ** 2
            if abs(sqrt-x) <= p:
                return mid
            elif sqrt < x:
                left = mid
            else:
                right = mid
        return left