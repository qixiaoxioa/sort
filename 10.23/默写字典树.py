class trieNode:
    def __init__(self):
        self.data = {}
        self.is_word = None
    def __repr__(self):
        return str(self.data)
class trie:
    def __init__(self):
        # 设置tries 树的根节点
        self.root = trieNode()
    def insert(self,word):
        node = self.root
        for char in word:
            child = node.data.get(char)
            if child is None:
               node.data[char] = trieNode()
            node = node.data[char]
        node.is_word = True

    #查询
    def search(self,word):
        node = self.root
        for char in word:
            child = node.data.get(char)
            if child is None:
                return False
        return node.is_word

    def prefix(self,prefix):
        node = self.root
        for char in prefix:
            child = node.data.get(char)
            if child is None:
                return False
        return node.is_word

