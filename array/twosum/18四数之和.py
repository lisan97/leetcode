class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.nSumTarget(nums,4,0,target)

    def nSumTarget(self,nums,n,start,target):
        sz = len(nums)
        res = []
        if n < 2 or sz < n:
            return res
        nums.sort()
        if n == 2:
            l = start
            r = sz - 1
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
                    res.append([left, right])
                    # 跳过所有重复的元素
                    while l < r and nums[l] == left:
                        l += 1
                    while l < r and nums[r] == right:
                        r -= 1
            #n > 2 时，递归计算 (n-1)Sum 的结果
        else:
            for i in range(start, sz):
                # 跳过第一个数字重复的情况，否则会出现重复结果
                if i > start and nums[i] == nums[i - 1]:
                    continue
                sub = self.nSumTarget(nums,n-1, i + 1, target - nums[i])
                # (n-1)Sum 加上 nums[i] 就是 nSum
                for tmp in sub:
                    tmp.append(nums[i])
                    res.append(tmp)
        return res