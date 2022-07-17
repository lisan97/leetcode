class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # 回溯法，将s分割成4段，并且每段要符合要求
        self.n = len(s)
        if self.n < 4 or self.n > 12:
            return []
        track = []
        self.res = []
        self.backtrack(s, 0, track)
        return self.res

    def backtrack(self, s, start, track):
        # 得确保已经分割完
        if len(track) == 4 and start == self.n:
            self.res.append('.'.join(track))
            return
        for i in range(start, self.n):
            p = s[start:i + 1]
            if not self.isValid(p):
                continue
            track.append(p)
            self.backtrack(s, i + 1, track)
            track.pop()

    def isValid(self, p):
        if p == '0':
            return True
        if p[0] == '0':
            return False
        p = int(p)
        if p > 0 and p < 256:
            return True
        return False