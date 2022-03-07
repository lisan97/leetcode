class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        #res 记录插入次数
        res = 0
        #need 变量记录右括号的需求量
        need = 0
        for c in s:
            if c == '(':
                need += 2
                #当遇到左括号时，若对右括号的需求量为奇数，需要插入 1 个右括号
                if need % 2 == 1:
                    # 插入一个右括号
                    res += 1
                    # 对右括号的需求减一
                    need -= 1
            else:
                need -= 1
                #意味着右括号太多了
                if need == -1:
                    need = 1
                    #需插入一个左括号
                    res += 1
        return res + need