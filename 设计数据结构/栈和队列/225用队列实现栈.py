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