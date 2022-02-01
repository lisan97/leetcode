class Solution(object):

    def __init__(self, n, blacklist):
        """
        :type n: int
        :type blacklist: List[int]
        """
        import random
        ## 白名单长度
        self.white = n - len(blacklist)
        self.dic = {}
        ## 将黑名单的值先添加到字典
        for b in blacklist:
            self.dic[b] = 0
        # 在黑名单区 要映射的指针
        last = n - 1
        for b in blacklist:
            # 黑名单中的值 已经在 黑名单的区间, 那么可以忽略
            if b >= self.white:
                continue
            # last对应的值已经在黑名单中，则需要跳过黑名单中的数字
            while last in self.dic:
                last -= 1
            self.dic[b] = last
            last -= 1

    def pick(self):
        """
        :rtype: int
        """
        # 在白名单部分随机挑选
        index = random.randint(0,self.white -1)
        # 如果在黑名单中, 那么就映射为白名单的值
        if index in self.dic:
            return self.dic[index]
        return index
