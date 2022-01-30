class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        left = 0
        right = 1
        for weight in weights:
            left = max(weight,left)
            right += weight
        while left < right:
            mid = left + (right - left) // 2
            if self.f(weights,mid) > days:
                left = mid + 1
            else:
                right = mid
            # if self.f(weights, mid) == days:
            #     right = mid
            # elif self.f(weights,mid) > days:
            #     left = mid + 1
            # elif self.f(weights,mid) < days:
            #     right = mid
        return left

    def f(self,weights,x):
        days = 1
        cur = 0
        for weight in weights:
            if cur + weight > x:
                days += 1
                cur = 0
            cur += weight
        return days