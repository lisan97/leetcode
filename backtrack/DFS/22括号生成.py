class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 路径：已经做出的选择
        # 选择列表：( or )
        # 还需记录( 和 )的多少
        # 结束条件：长度到达n
        # 合法：对于一个「合法」的括号字符串组合 p，必然对于任何 0 <= i < len(p) 都有：子串 p[0..i] 中左括号的数量都大于或等于右括号的数量。
        # 所以维护每时每刻剩余的left不能大于right就行
        self.res = []
        track = []
        # 可用的左括号和右括号数量初始化为 n
        left = n
        right = n
        self.backtrack(track, left, right)
        return self.res

    def backtrack(self, track, left, right):
        # 数量小于 0 肯定是不合法的
        if left < 0 or right < 0:
            return
        # 若左括号剩下的多，说明不合法
        if right < left:
            return
        # 当所有括号都恰好用完时，得到一个合法的括号组合
        if left == 0 and right == 0:
            self.res.append(''.join(track))
            return
        # 尝试放一个左括号
        track.append('(')
        self.backtrack(track, left - 1, right)
        track.pop()
        # 尝试放一个右括号
        track.append(')')
        self.backtrack(track, left, right - 1)
        track.pop()