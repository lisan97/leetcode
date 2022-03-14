class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        '''
        两次遍历
        从左往右遍历一遍，如果右边孩子的评分比左边的高，则右边孩子的糖果数更新为左边孩子的糖果数加 1；
        再从右往左遍历一遍，如果左边孩子的评分比右边的高，且左边孩子当前的糖果数不大于右边孩子的糖果数，则左边孩子的糖果数更新为右边孩子的糖果数加 1
        '''
        n = len(ratings)
        if n == 1:
            return 1
        nums = [1] * n
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                nums[i] = nums[i-1] + 1
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                nums[i] = max(nums[i],nums[i+1] + 1)
        return sum(nums)