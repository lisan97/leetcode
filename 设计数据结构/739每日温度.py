class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0]*len(temperatures)
        #这里放元素索引，而不是元素
        stack = []
        for i in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            #得到索引间距
            res[i] = stack[-1] - i if stack else 0
            stack.append(i)
        return res