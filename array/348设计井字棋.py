class TicTacToe(object):
    def __init__(self, n):
        self.size = n
        self.board = [[0 for _ in range(n)] for j in range(n)]

    def move(self, row, col, player):
        self.board[row][col] = player  # 先把棋子放下去
        if self.check(row, col, player):  # 再判断有没有胜者
            return player

        return 0

    def check(self, row, col, toe):
        row_valid, col_valid = True, True

        for i in range(self.size):
            if self.board[row][i] != toe:  # 遍历整行
                row_valid = False
            if self.board[i][col] != toe:  # 遍历整列
                col_valid = False

        if row != col and row + col != self.size - 1:  # 如果不需要判断对角线就已经可以返回了
            return row_valid or col_valid

        dia_valid1, dia_valid2 = False, False

        if row == col:  # 判断\对角线，特点是i == j
            dia_valid1 = True
            for i in range(self.size):
                if self.board[i][i] != toe:
                    dia_valid1 = False

        if row + col == self.size - 1:  # 判断/对角线，特点是i + j == n - 1
            dia_valid2 = True
            for i in range(self.size):
                if self.board[i][self.size - 1 - i] != toe:
                    dia_valid2 = False

        return row_valid or col_valid or dia_valid1 or dia_valid2

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)