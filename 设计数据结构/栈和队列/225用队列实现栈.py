class MyStack(object):

    def __init__(self):
        from collections import deque
        self.queue = deque()
        #记录队尾元素
        self.topitem = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        self.topitem = x


    def pop(self):
        """
        :rtype: int
        """
        size = len(self.queue)
        #把队列前面的都取出来再加入队尾，让之前的队尾元素排到队头
        while size > 2:
            self.queue.append(self.queue.popleft())
            size -= 1
        #记录新的队尾元素
        self.topitem = self.queue[0]
        self.queue.append(self.queue.popleft())
        return self.queue.popleft()


    def top(self):
        """
        :rtype: int
        """
        return self.topitem


    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue