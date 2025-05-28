from typing import List

class BacktrackingLeetCode:
    def letterCombinations(self, digits: str) -> list[str]:
        """ leecode #17 """

        res = []
        if len(digits) == 0:
            return res
        dig2let = {'1': (),
                   '2': ('a', 'b', 'c'),
                   '3': ('d', 'e', 'f'),
                   '4': ('g', 'h', 'i'),
                   '5': ('j', 'k', 'l'),
                   '6': ('m', 'n', 'o'),
                   '7': ('p', 'q', 'r', 's'),
                   '8': ('t', 'u', 'v'),
                   '9': ('w', 'x', 'y', 'z'),
                   '0': (' ')}

        if len(digits) == 1:
            return list(dig2let[digits[0]])

        def addLetter(i, s):
            if i != len(digits):
                for c in dig2let[digits[i]]:
                    addLetter(i + 1, s + c)
            else:
                res.append(s)
                return

        addLetter(0, '')
        return res

    def wordExists(self, board: list[list[str]], word: str) -> bool:
        """ leetcode #79 """

        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]

        def charFound(i, j, n) -> bool:
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) \
                or visited[i][j] or board[i][j] != word[n]:
                return False

            if n == len(word) - 1:
                return True
            else:
                visited[i][j] = True
                res = charFound(i + 1, j, n + 1) \
                    or charFound(i - 1, j, n + 1) \
                    or charFound(i, j + 1, n + 1) \
                    or charFound(i, j - 1, n + 1)
                visited[i][j] = False
                return res

        for i in range(len(board)):
            for j in range(len(board[i])):
                if charFound(i, j, 0):
                    return True

        return False

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """ leetcode #78 """

        res = []

        def addSubset(cur_s, i):
            if i == len(nums):
                res.append(cur_s[:])
                return

            cur_s.append(nums[i])
            addSubset(cur_s, i + 1)
            cur_s.pop()
            addSubset(cur_s, i + 1)

        addSubset([], 0)
        return res

    def subsets_generator(self, nums: List[int]):
        """ leetcode #78 implemented as generator """

        def addSubset(cur_s, i):
            if i == len(nums):
                yield cur_s[:]

            else:
                cur_s.append(nums[i])
                yield from addSubset(cur_s, i + 1)
                cur_s.pop()
                yield from addSubset(cur_s, i + 1)

        yield from addSubset([], 0)

    def combine(self, n: int, k: int) -> List[List[int]]:
        """ leetcode #77 """

        res = []

        def buildCombination(c, i):
            if len(c) == k:
                res.append(c[:])
                return

            for j in range(i, n + 1):
                buildCombination(c + [j], j + 1)

        buildCombination([], 1)
        return res

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """ leetcode #39 """

        res = []
        candidates.sort()

        def findComb(comb, idx):
            sc = sum(comb)
            if sc == target:
                res.append(comb[:])
                return

            for i in range(idx, len(candidates)):
                if sc + candidates[i] > target:
                    break
                findComb(comb + [candidates[i]], i)

        findComb([], 0)
        return res

if __name__ == '__main__':
    blc = BacktrackingLeetCode()
    # print(blc.wordExists([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], 'ABCCED'))
    # print(blc.combine(4, 2))
    print(blc.subsets([1, 2, 3]))
