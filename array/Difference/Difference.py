class Difference(object):
    def __init__(self,nums):
        self.diff = [0] * len(nums)
        #根据初始数组构造差分数组
        self.diff[0] = nums[0]
        for i in range(1,len(nums)):
            self.diff[i] = nums[i] - nums[i-1]

    def increment(self,i,j,val):
        self.diff[i] += val
        #当 j+1 >= diff.length 时，说明是对 nums[i] 及以后的整个数组都进行修改，那么就不需要再给 diff 数组减 val 了
        if j+1 < len(self.diff):
            self.diff[j+1] -= val

    def result(self):
        #根据差分数组构造结果数组
        res = [0] * len(self.diff)
        res[0] = self.diff[0]
        for i in range(1,len(self.diff)):
            res[i] = res[i-1] + self.diff[i]
        return res