class Solution(object):
    def minKnightMoves(self,x,y):
        from collections import deque
        '''
        bfs
        双向bfs
        x，y取正，在bfs的时候加限制，如果太左或者太下，就pass掉
        '''
        x = abs(x)
        y = abs(y)
        visited = set()
        direction = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]
        queue = deque([[0,0]])
        visited.add((0,0))
        step = 0
        while queue:
            sz = len(queue)
            for _ in range(sz):
                node = queue.popleft()
                i = node[0]
                j = node[1]
                if i == x and j == y:
                    return step
                for a,b in direction:
                    nx,ny = i + a, j + b
                    if (nx,ny) not in visited and nx > -2 and ny > -2:
                        visited.add((nx,ny))
                        queue.append([nx,ny])
            step += 1
        return -1

if __name__ == '__main__':
    print(Solution().minKnightMoves(x = 5, y = 5))