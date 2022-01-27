from Difference import Difference

class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        nums = [0] * n
        df = Difference(nums)
        for booking in bookings:
            i,j,val = booking[0]-1, booking[1]-1, booking[2]
            df.increment(i,j,val)
        return df.result()