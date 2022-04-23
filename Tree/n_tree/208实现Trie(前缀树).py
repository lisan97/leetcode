class TreeNode(object):
    def __init__(self):
        '''
        实现一个类，用来存放他的子结点，并标识有没有以该字母结尾的单词
        '''
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

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node is not None and node.isEnd #同时该node还得是结尾的node


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True