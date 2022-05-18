class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #建立一个长度为 32 的数组 counts ，通过以上方法可记录所有数字的各二进制位的 1 的出现次数
        count = [0] * 32
        for num in nums:
            for i in range(32):
                count[i] += num & 1 #更新第 i 位
                num >>= 1 #第 i 位 --> 第 i + 1 位
        res = 0
        m = 3
        #将 counts 各元素对 3 求余，则结果为 “只出现一次的数字” 的各二进制位。
        for i in range(32):
            res <<= 1 #左移 1 位
            res |= count[31-i] % m #得到 只出现一次的数字 的第 (31 - i) 位并恢复第 i 位的值到 res
        return res if count[31] % m == 0 else ~(res ^ 0xffffffff) #如果res为负,需要先将 0 - 32 位取反（即 res ^ 0xffffffff ），再将所有位取反（即 ~ ）