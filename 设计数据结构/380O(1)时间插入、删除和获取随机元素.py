class RandomizedSet(object):

    def __init__(self):
        import random
        self.array = []
        self.dic = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            return False
        # 若 val 不存在，插入到 nums 尾部,并记录 val 对应的索引值
        self.array.append(val)
        self.dic[val] = len(self.array) - 1
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            return False
        # 先拿到 val 的索引
        i = self.dic[val]
        # 将最后一个元素对应的索引修改为 i
        self.dic[self.array[-1]] = i
        # 交换val 和最后一个元素
        self.array[i], self.array[-1] = self.array[-1], self.array[i]
        # 在数组中删除元素 val
        self.array.pop()
        # 删除元素 val 对应的索引
        del self.dic[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.array)