class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.found = False
        self.m = len(board)
        self.n = len(board[0])
        if self.m == 1 and self.n == 1:
            return board[0][0] == word
        used = [[False]*self.n for _ in range(self.m)]
        for i in range(self.m):
            if self.found:
                break
            for j in range(self.n):
                if self.found:
                    break
                self.traverse(board,word,i,j,0,used)
        return self.found

    def traverse(self,board,word,i,j,start,used):
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return
        if start == len(word):
            self.found = True
            return
        if used[i][j] or self.found or board[i][j] != word[start]:
            return
        used[i][j] = True
        self.traverse(board,word,i-1,j,start+1,used)
        self.traverse(board,word,i+1,j,start+1,used)
        self.traverse(board,word,i,j-1,start+1,used)
        self.traverse(board,word,i,j+1,start+1,used)
        used[i][j] = False