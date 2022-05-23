class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        #用pre[i]来维护本身及上方连续1的个数，然后就把问题转换为了84题求每一行柱状图中最大矩形问题
        m = len(matrix)
        n = len(matrix[0])
        pre = [0] * (n+1)
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    pre[j] += 1
                else:
                    pre[j] = 0
            stack = [-1]
            for k in range(n+1):
                while pre[k] < pre[stack[-1]]:
                    index = stack.pop()
                    cur_height = pre[index]
                    cur_width = k - stack[-1] - 1
                    res = max(res,cur_height*cur_width)
                stack.append(k)
        return res