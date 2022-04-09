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
        num = 0
        sign = '+'
        while s:
            c = s.popleft()
            if c.isdigit():
                num = 10*num + int(c)
            if (not c.isdigit() and c != ' ') or not s:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    stack[-1] = int(stack[-1]/float(num))
                num = 0
                sign = c
        return sum(stack)