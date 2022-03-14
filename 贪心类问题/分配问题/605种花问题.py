class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        #增加一个头部和尾部从而不需要分情况讨论首尾的情况
        flowerbed = [0] + flowerbed + [0]
        res = 0
        for i in range(1,len(flowerbed)-1):
            if res == n:
                return True
            #如果前后和当前都为0，则可以种一棵，不需要管其他位置的情况
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                res += 1
                flowerbed[i] = 1
        return res == n