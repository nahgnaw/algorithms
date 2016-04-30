# -*- coding: utf-8 -*-

"""
Implement a trie with insert, search, and startsWith methods.
"""


class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.is_leaf = False
        self.children = [None] * 26


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        walk = self.root
        for ch in word:
            ind = ord(ch) - ord('a')
            if not walk.children[ind]:
                walk.children[ind] = TrieNode()
            walk = walk.children[ind]
        walk.is_leaf = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        walk = self.root
        for ch in word:
            ind = ord(ch) - ord('a')
            if not walk.children[ind]:
                return False
            walk = walk.children[ind]
        if walk.is_leaf:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        walk = self.root
        for ch in prefix:
            ind = ord(ch) - ord('a')
            if not walk.children[ind]:
                return False
            walk = walk.children[ind]
        return True

    def autocomplete(self, prefix):
        """
        Returns all the words that start with the
        prefix.
        :type prefix: str
        :rtype: list
        """
        def dfs(node, word):
            if node.is_leaf:
                results.append(word)

            for ind in xrange(len(node.children)):
                if node.children[ind] is not None:
                    dfs(node.children[ind], word + chr(ind + ord('a')))

        walk = self.root
        for ch in prefix:
            ind = ord(ch) - ord('a')
            if not walk.children[ind]:
                return []
            walk = walk.children[ind]

        results = []
        dfs(walk, prefix)
        return results


if __name__ == '__main__':
    # Your Trie object will be instantiated and called as such:
    trie = Trie()
    trie.insert("tree")
    trie.insert("trie")
    trie.insert("treemap")
    trie.insert('tap')
    print trie.search("treemap")
    # print trie.startsWith("tree")
    print trie.autocomplete('t')
