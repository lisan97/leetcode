class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        '''
        既然无法求整体的一个前缀和数组，可以分成若干块，求每块的和，这样求sumRange能从O(n)降为O(logn),更新为O(1)
        '''
        n = len(nums)
        self.size = int(n ** 0.5)
        self.sums = [0] * ((n + self.size - 1) // self.size)
        for i, num in enumerate(nums):
            self.sums[i // self.size] += num
        self.nums = nums

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.sums[index // self.size] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        b1 = left // self.size
        b2 = right // self.size
        if b1 == b2:
            return sum(self.nums[left:right + 1])
        return sum(self.nums[left:(b1 + 1) * self.size]) + sum(self.sums[b1 + 1:b2]) + sum(
            self.nums[b2 * self.size:right + 1])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)