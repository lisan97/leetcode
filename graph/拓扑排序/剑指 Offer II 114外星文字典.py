from collections import defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        all_nodes = set()
        for word in words:
            all_nodes = all_nodes.union(set(word))
        graph, degree, could = self.buildGraph(words)
        if not could:
            return ''
        #选择入度为0的点作为起点
        start = [node for node in all_nodes if degree[node] == 0]
        for node in start:
            for nextnode in graph[node]:
                degree[nextnode] -= 1
                #当人度为0时加入
                if degree[nextnode] == 0:
                    start.append(nextnode)
        return ''.join(start) if len(start) == len(all_nodes) else ''

    def buildGraph(self,words):
        graph = defaultdict(list)
        degree = defaultdict(int)
        could = True
        for word1, word2 in pairwise(words):
            for char1, char2 in zip(word1,word2):
                if char1 != char2:
                    graph[char1].append(char2)
                    degree[char2] += 1
                    break
            else:
                if len(word1) > len(word2):
                    could = False
                    return graph, degree, could
        return graph, degree, could