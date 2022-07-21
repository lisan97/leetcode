class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return []
        import math
        num = math.pow(10,n)
        return [i for i in range(1,int(num))]

class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        #全排列，先固定开头只能是1-9，再对于剩余的进行回溯全排列
        track = []
        self.res = []
        for digit in range(1,n+1):
            self.backtrack(track,0,digit)
        return self.res

    def backtrack(self,track,level,digit):
        if level == digit:
            self.res.append(int(''.join(track)))
            return
        if level == 0:
            for i in range(1,10):
                track.append(str(i))
                self.backtrack(track,level+1,digit)
                track.pop()
        else:
            for i in range(10):
                track.append(str(i))
                self.backtrack(track,level+1,digit)
                track.pop()