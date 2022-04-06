class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        import random
        self.nums = nums
        self.n = len(nums)


    def reset(self):
        """
        :rtype: List[int]
        """
        return self.nums


    def shuffle(self):
        """
        :rtype: List[int]
        """
        if not self.nums:
            return []
        shuffled = self.nums.copy()
        for i in range(self.n):
            j = random.randrange(i,self.n)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled