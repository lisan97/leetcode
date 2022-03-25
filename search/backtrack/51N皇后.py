class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.']*n for _ in range(n)]
        self.res = []
        self.backtrack(board,0)
        return self.res

    def backtrack(self,board,row):
        n = len(board)
        #触发结束条件
        if row == n:
            #python需要这样写才能正确放入东西
            self.res.append([''.join(t) for t in board])
            return
        for col in range(n):
            #排除不合法选择
            if not self.isvalid(board,row,col):
                continue
            #做选择
            board[row][col] = 'Q'
            #进入下一行决策
            self.backtrack(board,row+1)
            #撤销选择
            board[row][col] = '.'

    def isvalid(self,board,row,col):
        #左下方，右下方和正下方不用检查（还没放皇后）；因为一行只会放一个皇后，所以每行不用检查。
        n = len(board)
        #检查正上方是否有皇后互相冲突
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        #检查右上方是否有皇后互相冲突
        i = row - 1
        j = col + 1
        while i >= 0 and j <= n-1:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        #检查左上方是否有皇后互相冲突
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        return True