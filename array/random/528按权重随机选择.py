class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        import random
        #构建前缀和数组，偏移一位留给 preSum[0]
        self.array = [0]
        for i in range(len(w)):
            self.array.append(self.array[i] + w[i])
        self.n = len(self.array)

    def pickIndex(self):
        """
        :rtype: int
        """
        #应该在闭区间 [1, self.array[-1]] 中选择，因为前缀和数组中 0 本质上是个占位符
        target = random.randint(1,self.array[-1])
        left = 0
        right = self.n
        #搜索左侧边界的二分搜索:返回的这个值是 nums 中大于等于 target 的最小元素索引
        while left < right:
            mid = left + (right - left) // 2
            if self.array[mid] < target:
                left = mid + 1
            else:
                right = mid
        #最后对这个索引减一（因为前缀和数组有一位索引偏移）
        return left - 1