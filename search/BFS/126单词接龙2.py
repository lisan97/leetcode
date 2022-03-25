class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        from collections import deque, defaultdict
        wordset = set(wordList)
        self.res = []
        if len(wordset) == 0 or endWord not in wordset:
            return self.res
        queue = deque([beginWord])
        #记录beginword到达endword最短路径的各节点的后继节点
        neighbor = defaultdict(list)
        #记录总的visited
        visited = set([beginWord])
        #记录下一个step的元素，防止重复加入本层
        next_level_visited = set()
        found = False
        #第 1 步：使用广度优先遍历得到后继结点列表
        while queue and not found:
            sz = len(queue)
            for _ in range(sz):
                word = queue.popleft()
                word_list = list(word)
                for i in range(len(word_list)):
                    ori_char = word_list[i]
                    #将每一位替换成 26 个小写英文字母
                    for j in range(26):
                        word_list[i] = chr(ord('a')+j)
                        next_word = ''.join(word_list)
                        if next_word in wordset:
                            if next_word not in visited:
                                if next_word == endWord:
                                    found = True
                                # 避免下层元素重复加入本层的队列
                                if next_word not in next_level_visited:
                                    next_level_visited.add(next_word)
                                    queue.append(next_word)
                                neighbor[word].append(next_word)
                    word_list[i] = ori_char
            # 取两集合全部的元素（并集，等价于将 next_level_visited 里的所有元素添加到 visited 里）
            visited = visited.union(next_level_visited)
            next_level_visited.clear()
        if not found:
            return self.res
        #第 2 步：基于后继结点列表 ，使用回溯算法得到所有最短路径列表
        track = [beginWord]
        self.traverse(track,beginWord,endWord,neighbor)
        return self.res

    def traverse(self,track,beginWord,endWord,neighbor):
        if beginWord == endWord:
            self.res.append(track[:])
            return
        for nextword in neighbor[beginWord]:
            track.append(nextword)
            self.traverse(track,nextword,endWord,neighbor)
            track.pop()