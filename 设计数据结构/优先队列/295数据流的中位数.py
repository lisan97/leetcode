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

'''
follow up1 如果数据流中所有整数都在 0 到 100 范围内?
可以使用建立长度为 101 的桶，每个桶分别统计每个数的出现次数，同时记录数据流中总的元素数量，每次查找中位数时，先计算出中位数是第几位，从前往后扫描所有的桶得到答案。
这种做法相比于对顶堆做法，计算量上没有优势，更多的是空间上的优化。

follow up2 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
对于 1% 采用哨兵机制进行解决即可，在常规的最小桶和最大桶两侧分别维护一个有序序列，即建立一个代表负无穷和正无穷的桶。
'''