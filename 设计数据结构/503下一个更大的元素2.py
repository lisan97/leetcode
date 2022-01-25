class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n
        stack = []
        #模拟数组长度翻倍
        for i in range(2*n-1,-1,-1):
            # % 运算符求模（余数），来获得环形特效
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            res[i%n] = stack[-1] if stack else -1
            stack.append(nums[i%n])
        return res