class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        #x ^ 1s = ^x, 1s表示和他一样长的全由1组成的二进制数
        n = len(bin(num)[2:])
        a = int(''.join(['1' for _ in range(n)]),2)
        return num ^ a

#另一种写法
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = 1
        while a < num:
            a <<= 1
            a += 1
        return num ^ a