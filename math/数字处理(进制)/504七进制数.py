class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        f = ''
        s = ''
        if num == 0:
            return '0'
        if num < 0:
            num = -num
            f = '-'
        while num:
            a = num // 7
            b = num % 7
            s = str(b) + s
            num = a
        return f+s