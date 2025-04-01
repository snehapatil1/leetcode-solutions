class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_node = False
        self.link_count = 0
    
    def add_node(self, ch):
        if ch not in self.children:
            self.children[ch] = TrieNode()
            self.link_count += 1

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.add_node(ch)
            node = node.children[ch]
        node.is_end_node = True
    
    def get_longest_common_prefix(self, word):
        node = self.root
        chars = []
        for ch in word:
            if ch in node.children and not node.is_end_node and node.link_count == 1:
                chars.append(ch)
                node = node.children[ch]
            else:
                break
        return "".join(chars)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        word = strs[0]
        trie = Trie()
        for w in strs[1:]:
            trie.insert(w)
        return trie.get_longest_common_prefix(word)