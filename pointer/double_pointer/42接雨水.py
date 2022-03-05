#备忘录，时间O(n)，空间O(n)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 1:
            return 0
        #数组充当备忘录
        l_max = [0] * n
        r_max = [0] * n
        #初始化 base case
        l_max[0] = height[0]
        r_max[n-1] = height[n-1]
        #从左向右计算 l_max
        for i in range(1,n):
            l_max[i] = max(height[i],l_max[i-1])
        #从右向左计算 r_max
        for i in range(n-2,-1,-1):
            r_max[i] = max(height[i],r_max[i+1])
        res = 0
        #计算答案
        for i in range(n):
            res += min(l_max[i], r_max[i]) - height[i]
        return res

#双指针，时间O(n)，空间O(1)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 1:
            return 0
        i = 0
        j = n - 1
        res = 0
        l_max = 0
        r_max = 0
        while i <= j:
            l_max = max(height[i],l_max)
            r_max = max(height[j],r_max)
            #res += min(l_max, r_max) - height[i]
            if l_max < r_max:
                res += l_max - height[i]
                i += 1
            else:
                res += r_max - height[j]
                j -= 1
        return res