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
            if c == '(':
                num = self.help(s)
            if (not c.isdigit() and c != ' ') or not s:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                num = 0
                sign = c
            # 因为是在while里面，所以是break这个while循环而不是直接return
            if c == ')':
                break
        return sum(stack)