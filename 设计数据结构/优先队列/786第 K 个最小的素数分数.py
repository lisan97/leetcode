#O(n^2logk)
class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        from heapq import *
        hq = []
        for i in range(len(arr)-1):
            num1 = arr[i]
            for j in range(i+1,len(arr)):
                heappush(hq,(-num1/float(arr[j]),num1,arr[j]))
                if len(hq) > k:
                    _ = heappop(hq)
        return [hq[0][1],hq[0][2]]

#多路归并O(Klogn)
class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        from heapq import *
        hq = []
        n = len(arr)
        for i in range(1,n):
            heappush(hq,(arr[0]/float(arr[i]),0,i))
        while k>1:
            _, i,j = heappop(hq)
            if i + 1 < j:
                heappush(hq,(arr[i+1]/float(arr[j]),i+1,j))
            k -= 1
        return [arr[hq[0][1]],arr[hq[0][2]]]

#二分查找O(nlogC)
class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        self.eps = 1e-8
        self.n = len(arr)
        self.a = 0
        self.b = 0
        left = 0
        right = 1
        while right - left > self.eps:
            mid = (left + right) / 2.0
            num = self.check(arr,mid)
            if num >= k:
                right = mid
            else:
                left = mid
        return [self.a,self.b]

    def check(self,arr,mid):
        count = 0
        i = 0
        for j in range(1,self.n):
            while arr[i] / float(arr[j]) < mid:
                i += 1
            count += i
            if abs(arr[i]/float(arr[j])-mid) < self.eps:
                self.a = arr[i]
                self.b = arr[j]
        return count