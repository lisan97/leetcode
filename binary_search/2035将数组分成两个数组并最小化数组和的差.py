#数组太长时会超时
class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 用回溯算法遍历所有装一半的组合可能，取最小值
        self.total = sum(nums)
        self.n = len(nums)
        self.res = float('inf')
        self.backtrack(nums, 0, 0, 0)
        return self.res

    def backtrack(self, nums, start, cursum, curlen):
        if curlen == self.n // 2:
            curdiff = abs(2 * cursum - self.total)
            self.res = min(curdiff, self.res)
            return
        for i in range(start, self.n):
            curlen += 1
            self.backtrack(nums, i + 1, cursum + nums[i], curlen)
            curlen -= 1

#折半枚举，排序，二分
class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from itertools import combinations
        n = len(nums) // 2
        res = float('inf')
        total = sum(nums)
        target = total // 2
        for i in range(n):
            left_comb = sorted(sum(comb) for comb in combinations(nums[:n],i))
            right_comb = sorted(sum(comb) for comb in combinations(nums[n:],n-i))
            length = len(left_comb)
            left = 0
            right = length - 1
            while left <= length - 1 and right >= 0:
                cursum = left_comb[left] + right_comb[right]
                diff = abs(2*cursum-total)
                res = min(res,diff)
                if res == 0:
                    return res
                if cursum < target:
                    left += 1
                else:
                    right -= 1
        return res