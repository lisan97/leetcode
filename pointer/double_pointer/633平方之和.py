class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 0
        j = int(c**0.5)
        while i <= j:
            total = i**2+j**2
            if total > c:
                j -= 1
            elif total < c:
                i += 1
            else:
                return True
        return False