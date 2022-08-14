class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #碰到数字，检验该行、列、box内有无出现该数字就行
        #用哈希表解决row[i][j]=1代表第i行出现过j
        row = [[0] * 10 for _ in range(9)]
        col = [[0] * 10 for _ in range(9)]
        box = [[0] * 10 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j])
                if row[i][num] != 0 or col[j][num] != 0 or box[(i//3)*3+j//3][num] != 0:
                    return False
                row[i][num] = 1
                col[j][num] = 1
                box[(i//3)*3+j//3][num] = 1
        return True