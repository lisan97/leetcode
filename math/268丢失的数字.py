#HashSet 的解法时间复杂度是 O(N)，但是还需要 O(N) 的空间复杂度存储 HashSet
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = set([i for i in range(len(nums)+1)])
        return ans.difference(set(nums)).pop()

#异或运算 O(N)，空间复杂度O(1)
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        #先和新补的索引异或一下
        res = n
        #和其他的元素、索引做异或
        for i in range(n):
            res ^= i ^ nums[i]
        return res

#等差数列求和公式
#那这个数字不就是 sum(0,1,..n) - sum(nums)
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = n
        #剩下索引和元素的差加起来
        for i in range(n):
            res += i - nums[i]
        return res