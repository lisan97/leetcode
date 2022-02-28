class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        #16 = 1*16 = 2*8 = 4*4 16会亮，因为因子4重复出现，按了5次(奇数次)，所以找到那些平方根就行
        return int(n ** 0.5)