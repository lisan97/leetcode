class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {')':'(',']':'[','}':'{'}
        stack = []
        for c in s:
            if c in ['(','[','{']:
                stack.append(c)
            else:
                #和最近的左括号是否匹配
                if stack and stack[-1] == dic[c]:
                    stack.pop()
                else:
                    return False
        #是否所有的左括号都被匹配了
        return not stack