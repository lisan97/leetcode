class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        #但本题需要我们将从 11 开始，因此在执行「进制转换」操作前，我们需要先对 columnNumbercolumnNumber 执行减一操作，从而实现整体偏移。
        res = ''
        while columnNumber:
            columnNumber -= 1
            a = columnNumber // 26
            b = columnNumber % 26
            res = chr(ord('A') + b) + res
            columnNumber = a
        return res