from heapq import *
class MedianFinder(object):

    def __init__(self):
        self.small = []
        heapify(self.small)
        self.large = []
        heapify(self.large)

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        #这样就巧妙地保证了large堆整体大于small堆
        if len(self.small) >= len(self.large):
            heappush(self.small,-num)
            value = -heappop(self.small)
            heappush(self.large,value)
        else:
            heappush(self.large,num)
            value = -heappop(self.large)
            heappush(self.small,value)

    def findMedian(self):
        """
        :rtype: float
        """
        #如果元素不一样多，多的那个堆的堆顶元素就是中位数
        #因为python只有小顶堆，所以small内元素取负来实现大顶堆
        if len(self.small) > len(self.large):
            return - self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            #如果元素一样多，两个堆堆顶元素的平均数是中位数
            return (self.large[0]-self.small[0])/2.0