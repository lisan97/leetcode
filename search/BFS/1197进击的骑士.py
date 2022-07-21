class Solution(object):
    def minKnightMoves(self,x,y):
        '''
        bfs
        双向bfs
        x，y取正，在bfs的时候加限制，如果太左或者太下，就pass掉
        '''