class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        #从左往右遍历，同时记录当前的最大值，每当当前最大值等于数组位置时，我们可以多一次分割
        #如果当前最大值大于数组位置，则说明右边一定有小于数组位置的数字，需要把它也加入待排序的子数组；
        #又因为数组只包含不重复的 0 到 n，所以当前最大值一定不会小于数组位置
        count = 0
        cur_max = 0
        n = len(arr)
        for i in range(n):
            cur_max = max(arr[i],cur_max)
            if cur_max == i:
                count += 1
        return count