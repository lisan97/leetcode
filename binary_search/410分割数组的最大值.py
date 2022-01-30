class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        left = 0
        right = 1
        for num in nums:
            left = max(left,num)
            right += num
        while left < right:
            mid = left + (right - left)//2
            if self.f(nums,mid) > m:
                left = mid + 1
            else:
                right = mid
        return left
    #我们可以反过来，限制一个最大子数组和 max，来反推最大子数组和为 max 时，至少可以将 nums 分割成几个子数组。
    #那如果我们找到一个最小 max 值，满足 split(nums, max) 和 m 相等，那么这个 max 值不就是符合题意的「最小的最大子数组和」吗？
    def f(self,nums,mid):
        total = 0
        cnt = 1
        for num in nums:
            if total + num > mid:
                total = 0
                cnt += 1
            total += num
        return cnt
    #假设 nums 元素个数为 N，元素和为 S，则 split 函数的复杂度为 O(N)，二分查找的复杂度为 O(logS)，所以算法的总时间复杂度为 O(N*logS)