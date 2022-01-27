from Difference import Difference

class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        nums = [0] * 1001
        df = Difference(nums)
        for trip in trips:
            #第 trip[1] 站乘客上车
            #第 trip[2] 站乘客已经下车，
            #即乘客在车上的区间是 [trip[1], trip[2] - 1]
            val,i,j = trip[0],trip[1],trip[2]-1
            df.increment(i,j,val)
        res = df.result()
        for num in res:
            if num > capacity:
                return False
        return True