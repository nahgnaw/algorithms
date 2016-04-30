# -*- coding: utf-8 -*-

"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

Corner Cases:
A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.
"""


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        line = []
        char_count = 0
        for w in words:
            # char_count: number of current characaters
            # len(line): at least one space after each current word
            # len(word): length of the next word
            if char_count + len(line) + len(w) > maxWidth:
                # Insert a white space after each of the current words
                # except the last word
                for i in xrange(maxWidth - char_count):
                    line[i%(len(line)-1 or 1)] += ' '   # There can be only one word
                # Append the current line of word to the final result
                result.append(''.join(line))
                line = []
                char_count = 0
            
            line.append(w)
            char_count += len(w)
        return result + [' '.join(line).ljust(maxWidth)]
