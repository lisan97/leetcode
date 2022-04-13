class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #因为没有限制数值的大小，所以无法用本身数组的正负去判定，得额外用一个集合
        n = len(nums)
        m = len(set(nums))
        return not m == n