class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        '''
        最终会得到 11
        最终会进入循环
        '''
        #快慢指针检测环，并检测起点是否等于1，不要用哈希集合，节省空间复杂度
        fast,slow = self.getnext(n),n
        while fast != 1 and fast != slow:
            fast = self.getnext(self.getnext(fast))
            slow = self.getnext(slow)
        return fast == 1

    def getnext(self,num):
        total = 0
        while num > 0:
            num,digit = divmod(num,10)#除数和余数
            #求每一位平方的方式
            total += digit**2
        return total