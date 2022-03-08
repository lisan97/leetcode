class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        return self.help(collections.deque(s))

    def help(self,s):
        stack = []
        #记录算式中的数字
        num = 0
        #记录 num 前的符号，初始化为 +
        sign = '+'
        while s:
            c = s.popleft()
            #字符串转整数
            if c.isdigit():
                num = 10*num + int(c)
            # 遇到左括号开始递归计算 num
            if c == '(':
                num = self.help(s)
            #遇到符号或到头
            if (not c.isdigit() and c != ' ') or not s:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                #只要拿出前一个数字做对应运算即可
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    # python 除法向 0 取整的写法
                    stack[-1] = int(stack[-1]/float(num))
                #更新符号为当前符号，数字清零
                num = 0
                sign = c
            # 遇到右括号返回递归结果
            if c == ')':
                break
        return sum(stack)