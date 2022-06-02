class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        #数字,字母,[,]
        #遇到数字，作为乘数
        #遇到[开始递归
        #遇到字母，将字母放入list
        #遇到]结束递归
        from collections import deque
        return ''.join(self.helpdecode(deque(s)))


    def helpdecode(self,s):
        stack = []
        num = 0
        while s:
            c = s.popleft()
            if c.isdigit():
                num = 10*num + int(c)
            elif c == '[':
                stack.extend(num * self.helpdecode(s))
                num = 0
            elif c.isalpha():
                stack.append(c)
            elif c == ']':
                break
            else:
                continue
        return stack