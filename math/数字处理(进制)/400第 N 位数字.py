class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 1 #位数
        count = 9 #数字
        start = 1 #每digit位数的起始数字
        #1确定n所在的位数
        while n > count:
            n -= count
            digit += 1
            start *= 10
            count = 9 * start * digit
        #2确定n所在的数字(从第0位开始计数，所以要n-1)
        num = start + (n-1) // digit
        #3确定n所在数字的数位
        s = str(num)
        res = int(s[(n-1)%digit])
        return res