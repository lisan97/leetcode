class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #单调栈，删除数:n-k
        #当删除数达到上限时不能再删除
        #若遍历完之后，删除数还有多，把栈顶的pop出来
        n = len(nums)
        deleteNum = n - k
        stack = []
        for i in range(n):
            while stack and deleteNum > 0 and stack[-1] > nums[i]:
                stack.pop()
                deleteNum -= 1
            stack.append(nums[i])
        while deleteNum > 0:
            stack.pop()
            deleteNum -= 1
        return stack