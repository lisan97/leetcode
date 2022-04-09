class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #对输入 n 的二进制表示右移一位后，得到的数字再与 n 按位异或得到 a。当且仅当输入 n 为交替位二进制数时，a 的二进制表示全为 1
        #将 a 与 a+1 按位与，当且仅当 a 的二进制表示全为 1 时，结果为 0
        a = n^(n >> 1)
        return a & (a+1) == 0