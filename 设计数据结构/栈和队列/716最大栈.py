class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_stack = [] #维护栈顶为最大值

    def push(self, x):
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self):
        num = self.stack.pop()
        if num == self.max_stack[-1]:
            self.max_stack.pop()
        return num

    def top(self):
        return self.stack[-1]

    def peekMax(self):
        return self.max_stack[-1]

    def popMax(self):
        max_number = self.peekMax()
        buffer_s = [] #存放stack内在max_number之后的数，等到max_number pop出来以后再一个一个push进来
        while self.top() != max_number:
            buffer_s.append(self.pop())
        self.pop()
        while buffer_s:
            self.push(buffer_s.pop())
        return max_number