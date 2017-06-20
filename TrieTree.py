class TrieNode(object):
    def __init__(self):
        self.data = {}
        self.is_word = False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            child = node.data.get(letter)
            if not child:
                node.data[letter] = TrieNode()
            node = node.data[letter]
        node.is_word = True



    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for letter in word:
            if node.data.get(letter):
                node = node.data.get(letter)
            else:
                return False
        return node.is_word




    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for letter in prefix:
            if node.data.get(letter):
                node = node.data.get(letter)
            else:
                return False
        return True


        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)