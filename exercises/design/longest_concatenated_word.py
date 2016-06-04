# -*- coding: utf-8 -*-

"""longest_concatenated_word.py

Usage:
$ python longest_concatenated_word.py <input_file>

Developed under Python 2.7.11.

"""

import sys
import time

__author__ = 'Han Wang'
__email__ = 'wangh17@rpi.edu'


class Trie(object):
    """A trie data structure allowing fast string look-up."""

    class Node(object):
        """ A node in the trie."""
        def __init__(self, alphabet_size=26):
            self.is_leaf = False
            self.children = [None] * alphabet_size

    def __init__(self):
        self.root = Trie.Node()

    def _get_char_index(self, char, base='a'):
        """Helper function to return a character's index used to store it
        in a trie node.
        """
        return ord(char) - ord(base)

    def insert(self, word):
        """Insert the given word into the trie."""
        walk = self.root
        for ch in word:
            ind = self._get_char_index(ch)
            if not walk.children[ind]:
                walk.children[ind] = Trie.Node()
            walk = walk.children[ind]
        walk.is_leaf = True

    def search(self, word):
        """Return if the given word is in the trie."""
        walk = self.root
        for ch in word:
            ind = self._get_char_index(ch)
            if not walk.children[ind]:
                return False
            walk = walk.children[ind]
        return True if walk.is_leaf else False

    def is_concatenated(self, word):
        """Return if the given word is a concatenated by more than one word
        in the trie.
        """
        def dfs(suffix, parts):
            # Only return True if the word 
            # is concatenated by more than one word.
            if not suffix and len(parts) > 1:
                return True

            for i in xrange(1, len(suffix) + 1):
                if self.search(suffix[:i]):
                    if dfs(suffix[i:], parts + [suffix[:i]]):
                        return True
            return False

        return dfs(word, [])


if __name__ == '__main__':

    if not len(sys.argv) == 2:
        print 'Usage:\npython longest_concatenated_word.py <input_file>'
        exit(0)

    input_file = sys.argv[1]
    words = []
    with open(input_file) as f:
        for line in f:
            if line:
                line = line.strip()
                if line:
                    words.append(line)
    print 'Total number of words in the input file: {}'.format(len(words))

    start_time = time.time()

    print 'Constructing trie...'
    trie = Trie()
    for w in words:
        trie.insert(w)

    print 'Looking for concatenated words...'
    count = 0
    longest_len, sec_longest_len = 0, 0
    longest, sec_longest = [], []
    for w in words:
        if trie.is_concatenated(w):
            count += 1
            if len(w) >= longest_len:
                if len(w) == longest_len:
                    longest.append(w)
                else:
                    longest_len, sec_longest_len = len(w), longest_len
                    longest, sec_longest = [w], longest
            elif len(w) >= sec_longest_len:
                if len(w) == sec_longest_len:
                    sec_longest.append(w)
                else:
                    sec_longest_len = len(w)
                    sec_longest = [w]

    print 'Total number of concatenated words: {}'.format(count)
    print 'Longest concatenated word(s): {} (length: {})'.format(
        ', '.join(longest), longest_len)
    print 'Second longest concatenated word(s): {} (length: {})'.format(
        ', '.join(sec_longest), sec_longest_len)
    print 'Running time: {:.4f}s.'.format(time.time() - start_time)
