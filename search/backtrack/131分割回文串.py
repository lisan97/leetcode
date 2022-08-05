class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        #回溯，用valid函数判定是否是回文串
        self.res = []
        track = []
        self.n = len(s)
        self.backtrack(track,s,0)
        return self.res

    def backtrack(self,track,s,start):
        if start == self.n:
            self.res.append(track[:])
            return
        for i in range(start,self.n):
            p = s[start:i+1]
            if not self.isValid(p):
                continue
            track.append(p)
            self.backtrack(track,s,i+1)
            track.pop()

    def isValid(self,s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True