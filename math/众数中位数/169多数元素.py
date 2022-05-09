class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = nums[0]
        count = 1
        n = len(nums)
        if n == 1:
            return candidate
        for i in range(1,n):
            if candidate == nums[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                candidate = nums[i]
                count = 1
        return candidate

#partition函数找中间那个，但修改了数组，而且碰到特殊情况(已完全排序)会超时
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #用partition函数,找到中间那个数
        import random
        random.shuffle(nums)
        mid = len(nums) // 2
        l = 0
        r = len(nums) - 1
        p = self.partition(nums,l,r)
        while p != mid:
            p = self.partition(nums,l,r)
            if p < mid:
                l = p + 1
            else:
                r = p - 1
        return nums[p]

    def partition(self,nums,l,r):
        if l == r:
            return l
        p = nums[l]
        i = l+1
        j = r
        done = False
        while not done:
            while i <= j and nums[i] <= p:
                i += 1
            while i <= j and nums[j] >= p:
                j -= 1
            if i > j:
                done = True
            else:
                nums[i], nums[j] = nums[j], nums[i]
        nums[l] = nums[j]
        nums[j] = p
        return j