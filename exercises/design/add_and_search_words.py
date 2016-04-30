# -*- coding: utf-8 -*-

"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""


class WordDictionary(object):
    
    class Node(object):
        def __init__(self):
            self.children = [None] * 26
            self.is_leaf = False
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = WordDictionary.Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        walk = self.root
        for char in word:
            ind = ord(char) - ord('a')
            if walk.children[ind] is None:
                walk.children[ind] = WordDictionary.Node()
            walk = walk.children[ind]
        walk.is_leaf = True
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def dfs(walk, pos):
            if pos == len(word):
                return True if walk.is_leaf else False
                
            if word[pos] == '.':
                for child in walk.children:
                    if child:
                        if dfs(child, pos + 1):
                            return True
                return False
            else:
                char_ind = ord(word[pos]) - ord('a')
                if walk.children[char_ind]:
                    return dfs(walk.children[char_ind], pos + 1)
                else:
                    return False
            
        return dfs(self.root, 0)
        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")