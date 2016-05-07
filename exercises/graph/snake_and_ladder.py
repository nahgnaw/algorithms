# -*- coding: utf-8 -*-

"""
Given a snake and ladder board, find the minimum number of dice throws required to reach the destination or last cell from source or 1st cell. Basically, the player has total control over outcome of dice throw and wants to find out minimum number of throws required to reach last cell.

If the player reaches a cell which is base of a ladder, the player has to climb up that ladder and if reaches a cell is mouth of the snake, has to go down to the tail of snake without a dice throw.
"""


class Solution(object):
    def get_min_dice_throws(self, board, n):
        """
        :type board: List[int]
        :type n: int
        :rtype: int

        board is an array of size n where n is no. of cells on board.
        If there is no snake or ladder from cell i, then board[i] is -1
        Otherwise board[i] contains cell to which snake or ladder at i
        takes to.
        """
        from collections import deque

        visited = [False] * n

        # Every entry in the queue is a tuple (i, j) where i is the sequence no. of the board cell (i = 0, 1, ..., n-1)
        # and j is the minimum number of dice throws required to reach cell i from cell 0.
        queue = deque([(0, 0)]) # Put cell 0 into the queue.
        visited[0] = True

        # Start BFS from cell 0.
        while queue:
            cell = queue.popleft()

            # If this is the last cell, we are done.
            if cell[0] == n-1:
                return cell[1]

            # The next 6 cells can be reached with one dice throw.
            i = cell[0] + 1
            while i < n and i <= cell[0] + 6:
                if not visited[i]:
                    visited[i] = True
                    min_throws = cell[1] + 1
                    # If there is a ladder or a snake, replace the cell no.
                    if not board[i] == -1:
                        queue.append((board[i], min_throws))
                    queue.append((i, min_throws))
                i += 1


if __name__ == '__main__':
    sol = Solution()
    n = 30
    board = [-1] * n
    # Ladders
    board[2] = 21
    board[4] = 7
    board[10] = 25
    board[19] = 28
    # Snakes
    board[26] = 0
    board[20] = 8
    board[16] = 3
    board[18] = 6
    print sol.get_min_dice_throws(board, n)
