class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        '''
        如何设法将某块烧饼翻到最后？比如第 3 块饼是最大的
        1、用锅铲将前 3 块饼翻转一下，这样最大的饼就翻到了最上面。
        2、用锅铲将前 n 块饼全部翻转，这样最大的饼就翻到了第 n 块，也就是最后一块
        '''
        self.res = []
        self.cakesort(arr,len(arr))
        return self.res

    def cakesort(self,arr,n):
        #base case
        if n == 1:
            return
        #寻找最大饼的索引
        maxindex = 0
        maxCake = 0
        for i in range(n):
            if arr[i] > maxCake:
                maxCake = arr[i]
                maxindex = i
        #第一次翻转，将最大饼翻到最上面
        self.reverse(arr,0,maxindex)
        self.res.append(maxindex + 1)
        #第二次翻转，将最大饼翻到最下面
        self.reverse(arr,0,n-1)
        self.res.append(n)

        #递归调用
        self.cakesort(arr,n-1)

    def reverse(self,arr,i,j):
        while i < j:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i += 1
            j -= 1