class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1 #最小速度应该是 1
        right = 1000000000 + 1 #要么你用一个 for 循环去遍历piles数组，计算最大值;要么你看题目给的约束,给right初始化一个取值范围之外的值
        while left < right:
            mid = left + (right-left)//2
            if self.f(piles,mid) > h:
                left = mid + 1
            #建议合并多余的分支，可以提高算法运行的效率
            else:
                right = mid
            # if self.f(piles,mid) == h:
            #     right = mid
            # elif self.f(piles,mid) < h:
            #     right = mid
            # elif self.f(piles,mid) > h:
            #     left = mid + 1
        return left
    #要注意f是单调递增还是递减
    def f(self,piles,k):
        i = 0
        for num in piles:
            i += num // k
            if num % k > 0:
                i += 1
        return i