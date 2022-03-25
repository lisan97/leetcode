class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        #k 限制了树的高度，n 限制了树的宽度
        self.res = []
        track = []
        self.backtrack(n,k,track,0)
        return self.res

    def backtrack(self,n,k,track,start):
        if len(track) == k:
            self.res.append(track[:])
            return
        for i in range(start,n):
            track.append(i+1)
            self.backtrack(n,k,track,i+1)
            track.pop()