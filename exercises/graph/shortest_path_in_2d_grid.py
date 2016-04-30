# -*- coding: utf-8 -*-

"""
Given a 2d grid where 0 represents empty cells and 1 represents obstacles. Find the shortest path from two given cells.
"""


class Cell(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None


class Solution(object):
    def shortest_path(self, grid, start_x, start_y, end_x, end_y):

        def get_neighbors(cell):
            neighbors = []
            for x, y in [(cell.x - 1, cell.y), (cell.x, cell.y - 1), (cell.x + 1, cell.y), (cell.x, cell.y + 1)]:
                if 0 <= x < len(grid[0]) and 0 <= y < len(grid) and grid[x][y] == 0 and (x, y) not in visited:
                    visited.add((x, y))
                    n = Cell(x, y)
                    n.parent = cell
                    neighbors.append(n)
            return neighbors

        if not grid or not grid[0]:
            return 0

        from collections import deque

        start = Cell(start_x, start_y)

        visited = set([(start_x, start_y)])
        queue = deque([start])
        while queue:
            cell = queue.popleft()
            neighbors = get_neighbors(cell)
            for n in neighbors:
                if n.x == end_x and n.y == end_y:
                    path = [(n.x, n.y)]
                    while not n == start:
                        n = n.parent
                        path.append((n.x, n.y))
                    return path[::-1]
                queue.append(n)
        return None


if __name__ == '__main__':
    sol = Solution()
    grid = [
        [0,0,0,0],
        [1,0,0,0],
        [0,0,1,1],
        [0,0,0,0]
    ]        
    start_x, start_y = 0, 0
    end_x, end_y = 3, 0
    print sol.shortest_path(grid, start_x, start_y, end_x, end_y)
