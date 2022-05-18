class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        #排个序
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            #跳过第一个数字重复的情况，否则会出现重复结果
            if i > 0 and nums[i] == nums[i-1]:
                continue
            #对 target - nums[i] 计算 twoSum
            twores = self.twoSumtarget(nums,i+1,0-nums[i])
            #如果存在满足条件的二元组，再加上 nums[i] 就是结果三元组
            for tmp in twores:
                tmp.append(nums[i])
                res.append(tmp)
        return res


    def twoSumtarget(self,nums,start,target):
        l = start
        r = len(nums)-1
        res = []
        while l < r:
            left = nums[l]
            right = nums[r]
            total = left + right
            if total < target:
                while l < r and nums[l] == left:
                    l += 1
            elif total > target:
                while l < r and nums[r] == right:
                    r -= 1
            else:
                res.append([left,right])
                #跳过所有重复的元素
                while l < r and nums[l] == left:
                    l += 1
                while l < r and nums[r] == right:
                    r -= 1
        return res