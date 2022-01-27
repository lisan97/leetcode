class NumArray:

    def __init__(self, nums: list[int]):
        #preSum[0] = 0，便于计算累加和
        self.nums = [0] * (len(nums) + 1)
        for i in range(1,(len(nums)+1)):
            self.nums[i] = self.nums[i-1]+ nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right+1] - self.nums[left]