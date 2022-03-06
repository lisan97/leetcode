class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                #当遇到)但stack为空或者前一个不是(时
                if not stack or stack[-1] == ')':
                    stack.append(c)
                else:
                    stack.pop()
        return len(stack)

class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        #res 记录插入次数
        res = 0
        #need 变量记录右括号的需求量
        need = 0
        for c in s:
            if c == '(':
                need += 1
            else:
                need -= 1
                #意味着右括号太多了
                if need == -1:
                    need = 0
                    #需插入一个左括号
                    res += 1
        return res + need