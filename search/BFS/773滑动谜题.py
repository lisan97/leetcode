class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        from collections import deque
        m = len(board)
        n = len(board[0])
        start = ''
        #将 2x3 的数组转化成字符串作为 BFS 的起点
        for i in range(m):
            for j in range(n):
                start += str(board[i][j])
        target = '123450'
        #记录一维字符串的相邻索引
        neighbor = {0:[1,3],
                    1:[0,2,4],
                    2:[1,5],
                    3:[0,4],
                    4:[1,3,5],
                    5:[2,4]}
        q = deque([start])
        visited = set([start])
        step = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()
                if cur == target:
                    return step
                #找到数字 0 的索引
                idx = cur.index('0')
                #将数字 0 和相邻的数字交换位置
                for x in neighbor[idx]:
                    new_board = self.swap(list(cur),idx,x)
                    if new_board not in visited:
                        visited.add(new_board)
                        q.append(new_board)
            step += 1
        return -1

    def swap(self,chars,i,j):
        chars[i],chars[j] = chars[j],chars[i]
        return ''.join(chars)