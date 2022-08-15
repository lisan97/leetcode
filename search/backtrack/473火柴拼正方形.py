class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        #回溯算法找出4个和一样的火柴组合
        #先看看和能不能被4整除，不能的话直接返回False
        total = sum(matchsticks)
        if total % 4:
            return False
        self.n = len(matchsticks)
        target = total // 4
        matchsticks.sort()
        used = [False] * self.n
        self.memo = {}
        return self.backtrack(matchsticks,0,4,target,used,0)

    def backtrack(self,matchsticks,start,num,target,used,cur):
        if num == 0:
            return True
        key = tuple(used)
        if cur == 0:
            res = self.backtrack(matchsticks,0,num-1,target,used,target)
            self.memo[key] = res
            return res
        if key in self.memo:
            return self.memo[key]
        for i in range(start,self.n):
            if cur - matchsticks[i] < 0:
                break
            if used[i]:
                continue
            used[i] = True
            if self.backtrack(matchsticks,i+1,num,target,used,cur-matchsticks[i]):
                return True
            used[i] = False
        return False