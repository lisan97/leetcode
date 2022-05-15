class Solution(object):
    def __init__(self):
        self.res = 0

    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        #if(A && B)  // 若 A 为 false ，则 B 的判断不会执行（即短路），直接判定 A && B 为 false
        #通过短路效应来终止递归
        n > 1 and self.sumNums(n-1)
        self.res += n
        return self.res