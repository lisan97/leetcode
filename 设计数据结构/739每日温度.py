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
            # 直到 p 的温度小于栈顶存储位置的温度（或空栈）时，我们将 p 插入栈顶,并记录两个温度的索引之差
            # 在这个过程中，栈内数组永远保持单调递减，避免了使用排序进行比较。
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            #得到索引间距
            res[i] = stack[-1] - i if stack else 0
            stack.append(i)
        return res