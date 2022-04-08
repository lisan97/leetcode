class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        #每次把 res 左移，把 n 的二进制末尾数字，拼接到结果 res 的末尾。然后把 n 右移。
        res = 0
        for i in range(32):
            res <<= 1
            #n & 1得到n的最后一位
            res += n & 1
            n >>= 1
        return res