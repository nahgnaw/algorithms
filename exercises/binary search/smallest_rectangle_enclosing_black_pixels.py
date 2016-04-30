# -*- coding: utf-8 -*-

"""
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

For example, given the following image:

[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2,
Return 6.
"""


class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m, n = len(image), len(image[0])
        # search row range [0, x)
        top = self.search_rows(image, 0, x, True)
        # search row range [x + 1, len(image)]
        bottom = self.search_rows(image, x + 1, m, False)
        # search column range [0, y)
        left = self.search_columns(image, 0, y, top, bottom, True)
        # search column range [y+1, len(image[0]))
        right = self.search_columns(image, y + 1, n, top, bottom, False)
        print top, bottom, left, right
        return (top - bottom) * (left - right)

    def search_rows(self, arr, start, end, search_one):
        while start < end:
            mid = (start + end) / 2
            if ('1' in arr[mid]) == search_one:
                end = mid
            else:
                start = mid + 1
        return start

    def search_columns(self, arr, start, end, lower, upper, search_one):
        while start < end:
            mid = (start + end) / 2
            if any(arr[i][mid] == '1' for i in xrange(lower, upper)) == search_one:
                end = mid
            else:
                start = mid + 1
        return start


if __name__ == '__main__':
    image = [['0','0','1','0'],['0','1','1','0'],['0','1','0','0']]
    x, y = 0, 2
    sol = Solution()
    print sol.minArea(image, x, y)

