class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        #当碰到右侧有比自己低的，那么以自己起始的最大矩形大小就定了，所以可以用单调栈来存储之前的柱子(小到大)
        #同时在首尾先加两个0的哨兵，在循环中就不用做非空判断
        heights = heights + [0]
        n = len(heights)
        stack = [-1]
        res = 0
        for i in range(1,n):
            while heights[i] < heights[stack[-1]]:
                cur_hei = heights[stack.pop()]
                width = i - stack[-1] - 1#当前柱子和pop出的柱子的前一位和前一个柱子的宽度差，所以此时栈顶元素stack[-1]到k-1之间的数均是不小于heights[i]的
                area = cur_hei * width
                res = max(res,area)
            stack.append(i)
        return res