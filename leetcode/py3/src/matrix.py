from collections import deque
from typing import List, Optional

def print_grid(grid):
    print('\n')
    for r in grid:
        print(r)
    print('\n')

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    """ leetcode #54 """

    t, b, l, r = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

    res = []
    while t <= b and l <= r:
        i, j = t, l
        while j <= r:
            res.append(matrix[i][j])
            j += 1
        t += 1
        j -= 1
        i += 1
        if i > b: break
        while i <= b:
            res.append(matrix[i][j])
            i += 1
        r -= 1
        i -= 1
        j -= 1
        if j < l: break
        while j >= l:
            res.append(matrix[i][j])
            j -= 1
        b -= 1
        j += 1
        i -= 1
        if i < t: break
        while i >= t:
            res.append(matrix[i][j])
            i -= 1
        l += 1
        i += 1
        j += 1
        if j > r: break
    return res

def spiralOrderListPop(matrix: list[list[int]]) -> list[int]:
    """ leetcode #54 """

    res = []

    while matrix:
        res.extend(matrix.pop(0))

        if matrix and matrix[0]:
            for row in matrix:
                res.append(row.pop())

        if matrix:
            res.extend(matrix.pop()[::-1])

        if matrix and matrix[0]:
            for row in matrix[::-1]:
                res.append(row.pop(0))

    return res

def numIslands(grid: list[list[str]]) -> int:
    """ leetcode #200 """

    n = len(grid)
    m = len(grid[0])

    def destroyIsland(i: int, j: int):
        queue = deque([(i, j)])

        while queue:
            ci, cj = queue.popleft()
            if ci > 0 and grid[ci-1][cj] == '1':
                grid[ci-1][cj] = '0'
                queue.append((ci - 1,cj))
            if ci < n - 1 and grid[ci+1][cj] == '1':
                grid[ci+1][cj] = '0'
                queue.append((ci + 1, cj))
            if cj > 0 and grid[ci][cj-1] == '1':
                grid[ci][cj-1] = '0'
                queue.append((ci, cj - 1))
            if cj < m - 1 and grid[ci][cj+1] == '1':
                grid[ci][cj+1] = '0'
                queue.append((ci, cj + 1))
            grid[ci][cj] = '0'

    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                count += 1
                destroyIsland(i, j)
    return count

def shortestBridge(grid: List[List[int]]) -> int:
    """ leetcode #934 """

    n = len(grid)
    def paint_island(i: int, j: int):
        if i >= 0 and i < n and j >= 0 and j < n and grid[i][j] == 1:
            grid[i][j] = n + 1
            paint_island(i - 1, j)
            paint_island(i + 1, j)
            paint_island(i, j - 1)
            paint_island(i, j + 1)

    # find and paint the first island
    found_island = False
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                found_island = True
                paint_island(i, j)
                break
        if found_island:
            break

    def shortest_bridge(i: int, j: int) -> int:
        neighbors = deque([(i, j)])
        undo = []
        num_steps = 0
        def check_cell(i: int, j: int) -> bool:
            reached = False
            if i >= 0 and i < n and j >= 0 and j < n:
                if grid[i][j] == 1:
                    reached = True
                elif grid[i][j] == 0:
                    neighbors.append((i, j))
                    grid[i][j] = n + 2
                    undo.append((i, j))
            return reached

        reached = False
        while neighbors and not reached:
            num_steps += 1
            for _ in range(len(neighbors)):
                ni, nj = neighbors.popleft()
                if check_cell(ni - 1, nj):
                    reached = True
                elif check_cell(ni + 1, nj):
                    reached = True
                elif check_cell(ni, nj - 1):
                    reached = True
                elif check_cell(ni, nj + 1):
                    reached = True
                if reached:
                    break

        for ui, uj in undo:
            grid[ui][uj] = 0

        return num_steps - 1 if reached else n

    # walk the first island and find shortest path to second island
    min_bridge = n
    for i in range(n):
        for j in range(n):
            if grid[i][j] == n + 1:
                min_bridge = min(min_bridge, shortest_bridge(i, j))

    return min_bridge

