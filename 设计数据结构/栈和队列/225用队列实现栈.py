#一个队列
class MyStack(object):

    def __init__(self):
        from collections import deque
        self.queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)


    def pop(self):
        """
        :rtype: int
        """
        size = len(self.queue)
        #把队列前面的都取出来再加入队尾，让之前的队尾元素排到队头
        while size > 1:
            self.queue.append(self.queue.popleft())
            size -= 1
        return self.queue.popleft()


    def top(self):
        """
        :rtype: int
        """
        return self.queue[-1]


    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue

#两个队列
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        '''
        在入队列时进行操作，先将新元素放到q2，再将q1的元素放到q2，然后交换q1和q2，这时候新元素就在q1的最前面会先被pop
        '''
        from collections import deque
        self.queue1 = deque()
        self.queue2 = deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue1.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue1[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue1