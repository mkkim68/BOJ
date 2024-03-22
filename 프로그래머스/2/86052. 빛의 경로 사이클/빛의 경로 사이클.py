from collections import deque
from copy import deepcopy

def solution(grid):
    answer = []
    row, col = len(grid), len(grid[0])
    delta = deque([(1, 0), (0, 1), (-1, 0), (0, -1)])
    visited = set()
    for r in range(row):
        for c in range(col):
            for i in range(4):
                if ((r, c), delta[0]) not in visited:
                    visited.add(((r, c), delta[0]))
                    cur_delta = deepcopy(delta)
                    first_dir = cur_delta[0]
                    temp = deque()
                    cr, cc, cd = r, c, cur_delta[0]
                    while True:
                        temp.append(((cr, cc), cd))
                        now = grid[cr][cc]
                        if now == "S":
                            pass
                        elif now == "L":
                            cur_delta.rotate(-1)
                        elif now == "R":
                            cur_delta.rotate(1)
                        nd = cur_delta[0]
                        nr, nc = (cr + nd[0]) % row, (cc + nd[1]) % col
                        if nr == r and nc == c and cur_delta[0] == first_dir:
                            break
                        cr, cc, cd = nr, nc, nd
                    visited.update(set(temp))
                    answer.append(len(temp))
                delta.rotate(1)
    answer.sort()
    return answer
