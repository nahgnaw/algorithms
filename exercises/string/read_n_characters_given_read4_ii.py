# -*- coding: utf-8 -*-

"""
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.
"""


class Solution(object):
    def __init__(self):
        # Store characters returned by read4() outside read() 
        # such that they can be used by the next call of read().
        self.buf4 = [''] * 4    
        self.buf4_idx = 0   # Pointer in self.buf4
        self.buf4_cnt = 0   # Return value of read4()

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        index = 0
        while index < n:
            # If there is nothing left in self.buf4, read new data.
            # Else copy data from self.buf4 first
            if not self.buf4_idx:
                self.buf4_cnt = read4(self.buf4)
            if not self.buf4_cnt:
                return index
            while index < n and self.buf4_idx < self.buf4_cnt:
                buf[index] = self.buf4[self.buf4_idx]
                index += 1
                self.buf4_idx += 1
            if self.buf4_idx == self.buf4_cnt:
                self.buf4_idx = 0
        return index

