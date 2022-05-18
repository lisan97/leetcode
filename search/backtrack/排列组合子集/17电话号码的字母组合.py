class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        self.dic = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        self.length = len(digits)
        track = []
        self.res = []
        self.traverse(digits,0,track)
        return self.res

    def traverse(self,digits,start,track):
        if len(track) == self.length:
            self.res.append(''.join(track))
            return
        for c in self.dic[digits[start]]:
            track.append(c)
            self.traverse(digits,start + 1,track)
            track.pop()