class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        '''
        指针i和j和stack
        stack为空时,stack.append(pushed[i]),i+=1
        stack[-1] != popped[j]且i<n,stack.append(pushed[i]),i+=1
        stack[-1] != popped[j]且i==n,return False
        stack[-1] == popped[j]时,stack.pop(),j+=1
        '''
        if not pushed:
            return True
        stack = []
        n = len(pushed)
        i = 0
        j = 0
        #如果stack中有数或还没有push完
        while stack or i < n:
            #stack为空，直接往栈里压入数
            if not stack:
                stack.append(pushed[i])
                i += 1
            #栈顶元素不等于要pop的数
            elif stack[-1] != popped[j]:
                #还有还没入栈的数，将其压入栈
                if i < n:
                    stack.append(pushed[i])
                    i += 1
                #数都已经入栈了，则不是一个弹出序列
                else:
                    return False
            #栈顶的元素和要pop的数相等
            else:
                stack.pop()
                j += 1
        return True