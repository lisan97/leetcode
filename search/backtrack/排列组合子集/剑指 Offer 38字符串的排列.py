class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        '''
        全排列,每个字符只能用一次，字符串内可能有重复元素
        '''
        if not s:
            return []
        if len(s) == 1:
            return [s]
        s = sorted(list(s))
        self.n = len(s)
        used = [False] * self.n
        self.res = []
        track = []
        self.traverse(s,track,used)
        return self.res

    def traverse(self,s,track,used):
        if len(track) == self.n:
            self.res.append(''.join(track))
            return
        for i in range(self.n):
            if used[i]:
                continue
            if i != 0 and s[i] == s[i-1] and not used[i-1]:
                continue
            track.append(s[i])
            used[i] = True
            self.traverse(s,track,used)
            track.pop()
            used[i] = False