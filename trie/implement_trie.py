# Implement Trie (Prefix Tree)

# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

# Example 1:

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
 

# Constraints:

# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 104 calls in total will be made to insert, search, and startsWith.

class Node:
    def __init__(self):
        self.keys = {}
        self.end = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self._insert(word, self.root)
        
    def _insert(self, word, node):
        if not word:
            node.end = True
            return
        elif not word[0] in node.keys:
            node.keys[word[0]] = Node()
            self._insert(word[1:], node.keys[word[0]])
        else:
            self._insert(word[1:], node.keys[word[0]])
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self._search(word, self.root)

    def _search(self, word, node):
        if len(word) == 0 and node.end:
            return True
        elif len(word) == 0:
            return False
        elif not word[0] in node.keys:
            return False
        else:
            return self._search(word[1:], node.keys[word[0]])
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self._startsWith(prefix, self.root)
    
    def _startsWith(self, prefix, node):
        if not prefix:
            return True
        elif not prefix[0] in node.keys:
            return False
        else:
            return self._startsWith(prefix[1:], node.keys[prefix[0]])


# Your Trie object will be instantiated and called as such:
word = 'apple'
obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
print(param_2)
param_3 = obj.startsWith("app")
print(param_3)