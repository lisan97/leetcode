class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        from collections import deque
        if '0000' in deadends:
            return -1
        #记录已经穷举过的密码，防止走回头路，deadends可以直接加在visited里
        visited = set(deadends)
        visited.add('0000')
        queue = deque(['0000'])
        step = 0

        while queue:
            sz = len(queue)
            for _ in range(sz):
                cur = queue.popleft()
                if cur == target:
                    return step
                #就像每个节点有 8 个相邻的节点
                for j in range(4):
                    up = self.plusOne(cur,j)
                    if up not in visited:
                        queue.append(up)
                        visited.add(up)
                    down = self.minusOne(cur,j)
                    if down not in visited:
                        queue.append(down)
                        visited.add(down)
            step += 1
        #如果穷举完都没找到目标密码，那就是找不到了
        return -1

    def plusOne(self,s,j):
        s = list(s)
        if s[j] == '9':
            s[j] = '0'
        else:
            s[j] = str(int(s[j]) + 1)
        return ''.join(s)

    def minusOne(self,s,j):
        s = list(s)
        if s[j] == '0':
            s[j] = '9'
        else:
            s[j] = str(int(s[j]) - 1)
        return ''.join(s)

#双向BFS
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        from collections import deque
        if '0000' in deadends:
            return -1
        deads = set(deadends)
        visited = set()
        visited.add('0000')
        q1 = set()
        q2 = set()
        q1.add('0000')
        q2.add(target)
        step = 0

        while q1 and q2:
            #哈希集合在遍历的过程中不能修改，用 temp 存储扩散结果
            tmp = set()
            #将 q1 中的所有节点向周围扩散
            for cur in q1:
                if cur in deads:
                    continue
                if cur in q2:
                    return step
                visited.add(cur)
                #将一个节点的未遍历相邻节点加入集合
                for j in range(4):
                    up = self.plusOne(cur,j)
                    if up not in visited:
                        tmp.add(up)
                    down = self.minusOne(cur,j)
                    if down not in visited:
                        tmp.add(down)
            step += 1
            #temp 相当于 q1
            #这里交换 q1 q2，下一轮 while 就是扩散 q2
            q1 = q2
            q2 = tmp
        #如果穷举完都没找到目标密码，那就是找不到了
        return -1


    def plusOne(self,s,j):
        s = list(s)
        if s[j] == '9':
            s[j] = '0'
        else:
            s[j] = str(int(s[j]) + 1)
        return ''.join(s)

    def minusOne(self,s,j):
        s = list(s)
        if s[j] == '0':
            s[j] = '9'
        else:
            s[j] = str(int(s[j]) - 1)
        return ''.join(s)