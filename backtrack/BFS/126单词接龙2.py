class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        from collections import deque, defaultdict
        import string
        wordset = set(wordList)
        res = []
        if len(wordset) == 0 or endWord not in wordset:
            return res

        successors = defaultdict(set)
        # 第 1 步：使用广度优先遍历得到后继结点列表 successors
        found = self.bfs(beginWord, endWord, wordset, successors)
        if not found:
            return res
        # 第 2 步：基于后继结点列表 successors ，使用回溯算法得到所有最短路径列表
        path = [beginWord]
        self.dfs(beginWord, endWord, successors, path, res)
        return res

    def bfs(self, beginWord, endWord, wordset, successors):
        found = False
        visited = set([beginWord])
        queue = deque([beginWord])
        res = []
        word_len = len(beginWord)
        next_level_visited = set()
        while queue or not found:
            sz = len(queue)
            for i in range(sz):
                word = queue.popleft()
                word_list = list(word)
                for j in range(word_len):
                    ori_char = word_list[j]
                    for k in string.ascii_lowercase:
                        word_list[j] = k
                        next_word = ''.join(word_list)
                        if next_word in wordset:
                            if next_word not in visited:
                                if next_word == endWord:
                                    found = True
                                # 避免下层元素重复加入队列
                                if next_word not in next_level_visited:
                                    next_level_visited.add(next_word)
                                    queue.append(next_word)
                                successors[word].add(next_word)
                    word_list[j] = ori_char
            if found:
                break
            # 取两集合全部的元素（并集，等价于将 next_level_visited 里的所有元素添加到 visited 里）
            visited = visited.union(next_level_visited)
            next_level_visited.clear()
        return found

    def dfs(self, beginWord, endWord, successors, path, res):
        if beginWord == endWord:
            res.append(path[:])
            return
        if beginWord not in successors:
            return
        for next_word in successors[beginWord]:
            path.append(next_word)
            self.dfs(next_word, endWord, successors, path, res)
            path.pop()