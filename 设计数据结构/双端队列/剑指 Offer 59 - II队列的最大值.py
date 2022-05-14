class MaxQueue(object):

    def __init__(self):
        from collections import deque
        self.queue = deque()
        self.maxqueue = deque()

    def max_value(self):
        """
        :rtype: int
        """
        return self.maxqueue[0] if self.maxqueue else -1


    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.queue.append(value)
        while self.maxqueue and self.maxqueue[-1] < value:
            self.maxqueue.pop()
        self.maxqueue.append(value)


    def pop_front(self):
        """
        :rtype: int
        """
        if not self.queue:
            return -1
        val = self.queue.popleft()
        if val == self.maxqueue[0]:
            self.maxqueue.popleft()
        return val