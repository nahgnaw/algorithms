# -*- coding: utf-8 -*-

"""
You are given two cups that can hold exactly X and Y litres of water respectively. These two cups have no markings. You also have an unlimited supply of water.

You can only perform the following actions:

Fill a cup with water to its maximum volume.
Empty a cup.
Pour water from one cup to the other (until either the receiving cup is full or the pouring cup is empty).
Your task is find the minimum number of actions needed to measure out a given volume V of water using only these two cups. Your cups are always empty at the start.

Input

The first and only line of input contains three integer, X, Y, and V, in that order.

Output

Print the minimum number of actions needed, or -1 if it is impossible to achieve V.

E.g. X = 5, Y = 3, V = 4
One solution: (steps = 6)
5, 0
2, 3
2, 0
0, 2
5, 2
4, 3
"""


class Solution(object):
    def measure_volume(self, x, y, v):
        from collections import deque

        # steps[i][j]: the minimum steps required to fill i in the first cup and fill j in the second cup.
        steps = [[-1 for y in xrange(y + 1)] for _ in xrange(x + 1)]
        steps[0][0] = steps[x][y] = 0

        # An entry (i,j) in the queue means currently there is volume i in the first cup and volume j in the second cup.
        queue = deque()
        # We should start from (x, 0) or (0, y).
        queue.append((x, 0))
        queue.append((0, y))

        # Flag for if the problem is solved.
        finished = False
        # Counter for steps.
        step_count = 1

        while queue and not finished:
            queue_size = len(queue)
            for i in xrange(queue_size):
                cup1, cup2 = queue.popleft()

                if not steps[cup1][cup2] == -1:
                    continue
                elif cup1 == v or cup2 == v:
                    finished = True
                    return step_count
                else:
                    steps[cup1][cup2] = step_count

                    # We have four possible states:
                    # If cup1 is empty
                    if cup1 == 0:
                        # We can either fill up cup1 and do nothing to cup2
                        queue.append((x, cup2))
                        # or pour water from cup2 to cup1
                        if x < cup2:
                            queue.append((x, cup2 - x))
                        else:
                            queue.append((cup2, 0))

                    # If cup2 is emtpy
                    elif cup2 == 0:
                        # We can either fill up cup2 and do nothing to cup1
                        queue.append((cup1, y))
                        # or pour water from cup1 to cup2
                        if y < cup1:
                            queue.append((cup1 - y, y))
                        else:
                            queue.append((0, cup1))

                    # If cup1 is full
                    elif cup1 == x:
                        # We can either empty cup1 and do nothing to cup2
                        queue.append((0, cup2))
                        # or pour water from cup1 to cup2
                        if x < y - cup2:
                            queue.append((0, cup2 + x))
                        else:
                            queue.append((x - (y - cup2), y))

                    # If cup2 is full
                    elif cup2 == y:
                        # We can either empty cup2 and do nothing to cup1
                        queue.append((cup1, 0))
                        # or pour water from cup2 to cup1
                        if y < x - cup1:
                            queue.append((cup1 + y, 0))
                        else:
                            queue.append((x, y - (x - cup1)))
            step_count += 1

        if not finished:
            return -1
        

if __name__ == '__main__':
    sol = Solution()
    x, y, v = 5, 3, 4
    print sol.measure_volume(x, y, v)
