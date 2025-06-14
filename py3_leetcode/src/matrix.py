from collections import deque

def spiralOrder(matrix: list[list[int]]) -> list[int]:
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
