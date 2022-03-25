class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        track = []
        nums.sort()
        self.n = len(nums)
        self.used = [False] * self.n
        self.backtrack(nums,track)
        return self.res

    def backtrack(self,nums,track):
        if len(track) == self.n:
            self.res.append(track[:])
        for i in range(self.n):
            if self.used[i]:
                continue
            #保证相同元素在排列中的相对位置保持不变,2 -> 2' -> 2''，避免重复
            if i > 0 and nums[i] == nums[i-1] and not self.used[i-1]:
                continue
            self.used[i] = True
            track.append(nums[i])
            self.backtrack(nums,track)
            self.used[i] = False
            track.pop()