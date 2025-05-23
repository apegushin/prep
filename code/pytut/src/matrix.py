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

if __name__ == '__main__':
    mlc = MatrixLeetCode()
    # print(mlc.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(mlc.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))