class MyQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = [] #拿s2做中转，当要pop,peek的时候，若s2为空，反转s1中的数放入s2

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.s2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]


    def empty(self):
        """
        :rtype: bool
        """
        return not self.s1 and not self.s2