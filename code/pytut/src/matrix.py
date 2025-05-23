class MatrixLeetCode:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        t, b, l, r = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        res = []
        while t <= b and l <= r:
            i, j = t, l
            print(f't = {t}, b = {b}, l = {l}, r = {r}, i = {i}, j = {j}')
            while j <= r:
                print(f'going right adding {matrix[i][j]}, i = {i}, j = {j}')
                res.append(matrix[i][j])
                j += 1
            t += 1
            j -= 1
            i += 1
            if i > b: break
            while i <= b:
                print(f'going down adding {matrix[i][j]}, i = {i}, j = {j}')
                res.append(matrix[i][j])
                i += 1
            r -= 1
            i -= 1
            j -= 1
            if j < l: break
            while j >= l:
                print(f'going left adding {matrix[i][j]}, i = {i}, j = {j}')
                res.append(matrix[i][j])
                j -= 1
            b -= 1
            j += 1
            i -= 1
            if i < t: break
            while i >= t:
                print(f'going up adding {matrix[i][j]}, i = {i}, j = {j}')
                res.append(matrix[i][j])
                i -= 1
            l += 1
            i += 1
            j += 1
            if j > r: break
        return res

    def spiralOrderListPop(self, matrix: list[list[int]]) -> list[int]:
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

    def numIslands(self, grid: list[list[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def destroyIsland(i: int, j: int):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == '0':
                return

            grid[i][j] = '0'
            destroyIsland(i - 1, j)
            destroyIsland(i + 1, j)
            destroyIsland(i, j - 1)
            destroyIsland(i, j + 1)

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    destroyIsland(i, j)
        return count


if __name__ == '__main__':
    mlc = MatrixLeetCode()
    # print(mlc.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    # print(mlc.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    print(mlc.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))