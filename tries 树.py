class TrieNode:
    def __init__(self):
        self.data = {}
        self.is_word = None
    def __repr__(self):
        return str(self.data)

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        # 从根节点开始判断
        node = self.root
        for char in word:
            child = node.data.get(char)    #通过K得到他的value值.get(k)
            if child is None:
                node.data[char] = TrieNode()
            node = node.data[char]
        node.is_word = True

    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.data:
                return False
            node = node.data[char]
        return node.is_word

    def search1(self,word):
        node = self.root
        for char in word:
            node = node.data.get(char)
            if not node:
                return False
        return node.is_word

#     判断前缀存在与否
    def startWith(self,prefix):
        node = self.root
        for char in prefix:
            node = node.data.get(char)
            if not node:
                return False
        return True

if __name__ == '__main__':
    tri = Trie()
    tri.insert('something')
    tri.insert('somewhere')
    tri.insert('somebody')
    print(tri.search1('some'))

