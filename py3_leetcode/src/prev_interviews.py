from collections import deque
from typing import List, Tuple

def cd_dir(cur_wd: str, cdto: str) -> str:
    if len(cdto) == 0: return cur_wd

    if cdto.startswith('/'):
        cur_wd = ''
        cdto = cdto[1:]

    res_stack = deque(cur_wd[1:].split('/') if len(cur_wd) > 1 else [])
    for e in cdto.split('/'):
        if e == '.' or (e == '..' and len(res_stack) == 0):
            continue
        elif e == '..' and len(res_stack) > 0:
            res_stack.pop()
        else:
            res_stack.append(e)
    return '/' + '/'.join(list(res_stack))

def shortestPath(board: List[List[int]]) -> List[Tuple]:
    m = len(board)
    if m == 0: return []
    n = len(board[0])
    if n == 0: return []
    if board[0][0] == 1 or board[m-1][n-1] == 1: return []

    def min_path(i1: int, j1: int, i2: int, j2: int, accum: List[Tuple]) -> List[Tuple]:
        if i2 == m - 1 and j2 == n - 1:
            accum.append((i2, j2))
            return accum[:]
        else:
            if i2 >= 0 and i2 < m and j2 >= 0 and j2 < n and board[i2][j2] == 0:
                accum.append((i2, j2))
                board[i2][j2] = 2
                p1 = min_path(i2, j2, i2 - 1, j2, accum)
                p2 = min_path(i2, j2, i2 + 1, j2, accum)
                p3 = min_path(i2, j2, i2, j2 - 1, accum)
                p4 = min_path(i2, j2, i2, j2 + 1, accum)
                board[i2][j2] = 0
                accum.pop()
                paths = []
                if len(p1) > 0: paths.append(p1)
                if len(p2) > 0: paths.append(p2)
                if len(p3) > 0: paths.append(p3)
                if len(p4) > 0: paths.append(p4)
                return min(paths, key=len) if len(paths) > 0 else []
            else:
                return []

    board[0][0] = 2
    p1 = min_path(0, 0, 0, 1, [(0, 0)])
    p2 = min_path(0, 0, 1, 0, [(0, 0)])
    board[0][0] = 0
    paths = []
    if len(p1) > 0: paths.append(p1)
    if len(p2) > 0: paths.append(p2)
    return min(paths, key=len)
