class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        import random
        self.nums = nums
        self.n = len(nums)


    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res = -1
        count = 0
        for i in range(self.n):
            if self.nums[i] == target:
                # 生成一个 [0, count] 之间的整数
                # 这个整数等于 0 的概率就是 1/count
                n = random.randint(0,count)
                if n == 0:
                    res = i
                count += 1
        return res

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        from collections import defaultdict
        import random
        self.dic = defaultdict(list)
        for i,num in enumerate(nums):
            self.dic[num].append(i)


    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.dic[target])