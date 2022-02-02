class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import defaultdict
        #维护一个计数器记录字符串中字符的数量
        count = defaultdict(int)
        #通过inStack这个布尔数组做到栈stk中不存在重复元素。因为输入为 ASCII 字符，大小 256 够用了
        instack = [False] * 256
        #通过「栈」这种顺序结构的 push/pop 操作记录结果字符串，保证了字符出现的顺序和s中出现的顺序一致。
        stack = []
        for c in s:
            count[ord(c)] += 1
        for c in s:
            c = ord(c)
            #每遍历过一个字符，都将对应的计数减一
            count[c] -= 1
            if instack[c]:
                continue
            #插入之前，和之前的元素比较一下大小,如果字典序比前面的小，pop 前面的元素
            while stack and stack[-1] > c:
                #若之后不存在栈顶元素了，则停止 pop
                if count[stack[-1]] == 0:
                    break
                #若之后还有，则可以 pop
                instack[stack.pop()] = False
            stack.append(c)
            instack[c] = True
        stack = [chr(i) for i in stack]
        return ''.join(stack)