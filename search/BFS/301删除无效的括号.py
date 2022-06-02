class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        #使用bfs，这道题说的是删除最少的括号,如果我们每次只删除一个括号，然后观察被删除一个括号后是否合法，如果已经合法了，我们就不用继续删除了
        #上一层level和下一层level之间的关系为：把所有上一层level中的每个元素都拿出来，列举出在删除一个括号后的所有可能的情况
        #每轮刚开始的时候检查这层有没有出现合法的括号
        level = set()
        level.add(s)
        while True:
            #检查该层是否已经有符合条件的括号
            valid = list(filter(self.isValid,level))
            if valid:
                return valid
            nextlevel = set()
            #遍历所有删除的可能性
            for char in level:
                for i in range(len(char)):
                    if char[i] in '()':
                        nextlevel.add(char[:i]+char[i+1:])
            level = nextlevel


    def isValid(self,char):
        count = 0
        for c in char:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
                if count < 0:
                    return False
            else:
                continue
        return count == 0