class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        '''
        若拼接字符串 x+y>y+x ，则 x “大于” y ；
        反之，若x+y<y+x ，则 x “小于” y ；
        '''
        import functools
        def sort_rule(x,y):
            a = x+y
            b = y+x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0
        strs = [str(num) for num in nums]
        strs.sort(key=functools.cmp_to_key(sort_rule))
        return ''.join(strs)