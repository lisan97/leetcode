class TreeNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie(object):

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TreeNode()
            node = node.children[c]
        node.isEnd = True

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        tree = Trie()
        for s in strs:
            if not s:
                return ''
            tree.insert(s)
        res = ''
        node = tree.root
        while len(node.children) == 1 and not node.isEnd:
            c = list(node.children.keys())[0]
            res += c
            node = node.children[c]
        return res

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        if n == 1:
            return strs[0]
        prefix = strs[0]
        for i in range(1,n):
            prefix = self.lcp(prefix,strs[i])
            if not prefix:
                return ''
        return prefix

    def lcp(self,prefix,s):
        length = min(len(prefix),len(s))
        i = 0
        while i < length and prefix[i] == s[i]:
            i += 1
        return prefix[:i]