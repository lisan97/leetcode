#时间复杂度O(klogn)
#空间复杂度O(n)
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        #合并n个链表
        from heapq import *
        hq = []
        n = len(matrix)
        for i in range(n):
            heappush(hq,(matrix[i][0],i,0))
        while k > 0:
            num, i, j = heappop(hq)
            if j < n-1:
                heappush(hq,(matrix[i][j+1],i,j+1))
            k -= 1
        return num

#时间复杂度O(nlog(r−l))
#空间复杂度O(1)
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        #二分查找左边界
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left < right:
            mid = (left+right) // 2
            num = self.count(matrix,mid)
            if num >= k:
                right = mid
            else:
                left = mid + 1
        return left

    #从左下往右上寻找，不大于mid的数量
    def count(self,matrix,mid):
        n = len(matrix)
        i = n - 1
        j = 0
        num = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= mid:
                num += i + 1
                j += 1
            else:
                i -= 1
        return num
