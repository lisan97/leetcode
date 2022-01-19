from UF import UF
#DFS
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        self.m = len(board)
        self.n = len(board[0])
        self.board = board
        for i in range(self.n):
            self.traverse(0, i)
            self.traverse(self.m - 1, i)
        # 先用 for 循环遍历棋盘的四边，用 DFS 算法把那些与边界相连的 O 换成一个特殊字符，比如 #
        for i in range(1, self.m - 1):
            self.traverse(i, 0)
            self.traverse(i, self.n - 1)
        # 然后再遍历整个棋盘，把剩下的 O 换成 X，把 # 恢复成 O
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == 'O':
                    self.board[i][j] = 'X'
                elif self.board[i][j] == '#':
                    self.board[i][j] = 'O'
                else:
                    continue

        return self.board

    def traverse(self, x, y):
        # base case
        # board[x][y] != 'O'包含了board[x][y] == 'A'这种visited的情况，所以不需要visited数组来记录有无遍历过
        if not 0 <= x < self.m or not 0 <= y < self.n or self.board[x][y] != 'O':
            return
        self.board[x][y] = '#'
        self.traverse(x - 1, y)
        self.traverse(x + 1, y)
        self.traverse(x, y - 1)
        self.traverse(x, y + 1)

#UF
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board)
        n = len(board[0])
        #给 dummy 留一个额外位置
        uf = UF(m*n+1)
        dummy = m*n
        #将首列和末列的 O 与 dummy 连通
        for i in range(m):
            if board[i][0] == 'O':
                uf.union(dummy,i*n)
            if board[i][n-1] == 'O':
                uf.union(dummy,i*n+n-1)
        #将首行和末行的 O 与 dummy 连通
        for i in range(1,n-1):
            if board[0][i] == 'O':
                uf.union(dummy,i)
            if board[m-1][i] == 'O':
                uf.union(dummy,(m-1)*n+i)
        #方向数组 d 是上下左右搜索的常用手法
        d = [[1,0],[0,1],[-1,0],[0,-1]]
        for i in range(1,m-1):
            for j in range(1,n-1):
                if board[i][j] == 'O':
                    #将此 O 与上下左右的 O 连通
                    for a in range(4):
                        x = i+d[a][0]
                        y = j+d[a][1]
                        if board[x][y] == 'O':
                            uf.union(i*n+j,x*n+y)
        #所有不和 dummy 连通的 O，都要被替换
        for i in range(1,m-1):
            for j in range(1,n-1):
                if board[i][j] == 'O':
                    if not uf.connected(dummy,i*n+j):
                        board[i][j] = 'X'
        return board