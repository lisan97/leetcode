class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #我们可以把所有数字放到一个集合，
        #然后不断地从哈希表中任意取一个值，并删除掉其之前之后的所有连续数字
        #然后更新目前的最长连续序列长度。
        nums = set(nums)
        res = 0
        while nums:
            cur = nums.pop()
            pre = cur - 1
            nex = cur + 1
            while pre in nums:
                nums.remove(pre)
                pre -= 1
            while nex in nums:
                nums.remove(nex)
                nex += 1
            res = max(res,nex-pre-1)
        return res