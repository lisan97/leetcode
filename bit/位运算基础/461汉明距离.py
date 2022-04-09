class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #用异或统计有多少个不同的1
        return bin(x ^ y).count('1')