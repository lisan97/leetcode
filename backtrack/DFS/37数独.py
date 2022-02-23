#这个 O(9^M) 的复杂度实际上是完全穷举，或者说是找到所有可行解的时间复杂度
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        #j==n时则开始遍历下一行
        #遇到预设数字，过
        #判断这个选择是否valid
        #当i==n时结束
        self.n = len(board)
        self.board = board
        self.backtrack(0,0)
        return self.board

    def backtrack(self,i,j):
        #找到一个可行解，触发 base case
        if i == self.n:
            return True
        #穷举到最后一列的话就换到下一行重新开始。
        if j == self.n:
            return self.backtrack(i+1,0)
        #如果有预设数字，不用我们穷举
        if self.board[i][j] != '.':
            return self.backtrack(i,j+1)

        for ch in range(1,self.n+1):
            #如果遇到不合法的数字，就跳过
            if not self.isValid(i,j,str(ch)):
                continue
            self.board[i][j] = str(ch)
            #如果找到一个可行解，立即结束
            if self.backtrack(i,j+1):
                return True
            self.board[i][j] = '.'
        #穷举完 1~9，依然没有找到可行解，此路不通
        return False

    def isValid(self,r,c,ch):
        for i in range(self.n):
            if self.board[r][i] == ch:
                return False
            if self.board[i][c] == ch:
                return False
            #判断 3 x 3 方框是否存在重复
            if self.board[(r//3)*3+i//3][(c//3)*3+i%3] == ch:
                return False
        return True