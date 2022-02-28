class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #谁面对 4 的倍数，谁输
        return n % 4 != 0