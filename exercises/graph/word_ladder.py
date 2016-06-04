# -*- coding: utf-8 -*-

"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
"""


class Solution(object):
    # Bidirectional BFS.
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        length = 2
        chars = 'abcdefghijklmnopqrstuvwxyz'
        source, target = set([beginWord]), set([endWord])
        wordList.add(endWord)
        while source:
            # Generate all the transformations.
            pool = set(word[:i] + c + word[i+1:] for word in source for i in xrange(len(beginWord)) for c in chars)
            source = wordList & pool
            # If there is intersection between source and target, we are done.
            if source & target:
                return length
            length += 1
            # Swap for a smaller source set in order to have a smaller transformation pool.
            if len(source) > len(target):
                source, target = target, source
            # Remove seen transformations from wordList to avoid cycles.
            wordList -= source
        return 0
        


if __name__ == '__main__':
    beginWord = "cat"
    endWord = "fin"
    wordList = set(["ion","rev","che","ind","lie","wis","oct","ham","jag","ray","nun","ref","wig","jul","ken","mit","eel","paw","per","ola","pat","old","maj","ell","irk","ivy","beg","fan","rap","sun","yak","sat","fit","tom","bug","can","hes","col","pep","tug","ump","arc","fee","lee","ohs","eli","nay","raw","lot","mat","egg","cat","pol","fat","joe","pis","dot","jaw","hat","roe","ada","mac"])
    sol = Solution()
    print sol.ladderLength(beginWord, endWord, wordList)
