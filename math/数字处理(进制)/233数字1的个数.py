class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        将 1 ~ n的个位、十位、百位、...的 1 出现次数相加，即为 1 出现的总次数。
        if cur == 0: res += high * digit
        elif cur == 1: res += high * digit + low + 1
        else: res += (high + 1) * digit
        '''
        if n <= 0:
            return 0
        digit = 1 # 个位
        res = 0
        high = n // 10
        cur = n % 10
        low = 0
        while high != 0 or cur != 0:#当 high 和 cur 同时为 0 时，说明已经越过最高位，因此跳出
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high+1) * digit
            low += cur * digit # 将 cur 加入 low ，组成下轮 low
            cur = high % 10 # 下轮 cur 是本轮 high 的最低位
            high //= 10 # 将本轮 high 最低位删除，得到下轮 high
            digit *= 10 # 位因子每轮 × 10
        return res