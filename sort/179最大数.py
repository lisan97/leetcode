class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        import functools
        def sort_rule(x,y):
            a = x + y
            b = y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0
        nums = [str(i) for i in nums]
        nums.sort(key=functools.cmp_to_key(sort_rule),reverse=True)
        res = ''.join(nums).lstrip('0')
        return res if res else '0'