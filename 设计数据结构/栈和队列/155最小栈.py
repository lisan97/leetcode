class MinStack(object):

    def __init__(self):
        self.minS = []#用栈顶存储最小值
        self.s = []


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.s.append(val)
        #每次插入原栈时，都向新栈插入一次原栈里所有值的最小值（新栈栈顶和待插入值中小的那一个）
        #如果不每次都插入，bad case:s= [0,1,0],minS=[0],pop一次之后minS就为空了，但其实s里还有一个0
        if not self.minS or self.minS[-1] >= val:
            self.minS.append(val)


    def pop(self):
        """
        :rtype: None
        """
        num = self.s.pop()
        #每次从原栈里取出数字时，同样取出新栈的栈顶
        if self.minS and num == self.minS[-1]:
            self.minS.pop()
        return num


    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.minS[-1]