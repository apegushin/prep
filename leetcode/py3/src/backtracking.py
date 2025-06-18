from typing import List
import time

def letterCombinations(digits: str) -> list[str]:
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

def wordExists(board: list[list[str]], word: str) -> bool:
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

def subsets(nums: List[int]) -> List[List[int]]:
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

def subsets_generator(nums: List[int]):
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

def combine(n: int, k: int) -> List[List[int]]:
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

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
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

def wordBreak(s: str, wordDict: List[str]) -> bool:
    """ leetcode #139 """

    if len(s) == 0: return False

    wordSet = set(wordDict)
    words = []
    def breakWords(s: str) -> bool:
        if s == '':
            return True
        for i in range(1, len(s) + 1):
            if s[0:i] in wordSet:
                words.append(s[0:i])
                if breakWords(s[i:]):
                    return True
                words.pop()
        return False

    return breakWords(s)

def restoreIpAddresses_naive(s: str) -> List[str]:
    """ leetcode #93 """

    res = []
    if len(s) < 4 or len(s) > 12:
        return res

    accum = []
    def is_valid_ip() -> bool:
        for ip_num in ''.join(accum).split('.'):
            if (len(ip_num) == 0
                or (ip_num[0] == '0' and len(ip_num) > 1)
                or (int(ip_num) > 255)):
                return False
        return True

    def buildIpAddr(pos: int, dots_left: int):
        if dots_left == 0 and pos == len(s) and is_valid_ip():
            res.append(''.join(accum))
            return

        if dots_left > 0 and len(accum) > 0 and accum[-1] != '.':
            accum.append('.')
            buildIpAddr(pos, dots_left - 1)
            accum.pop()

        if pos < len(s):
            accum.append(s[pos])
            buildIpAddr(pos + 1, dots_left)
            accum.pop()

    buildIpAddr(0, 3)
    return res

def restoreIpAddresses(s: str) -> List[str]:
    """ leetcode #93 """

    res = []
    if len(s) < 4 or len(s) > 12:
        return res

    def is_valid_ipaddr_num(num_str: str) -> bool:
        return not (len(num_str) == 0 or len(num_str) > 3
            or (num_str[0] == '0' and len(num_str) > 1)
            or (int(num_str) > 255))

    def buildIpAddr(accum: str, s: str, dots_left: int):
        if len(s) == 0 and dots_left == -1:
            res.append(accum)
            return
        if dots_left == -1:
            return

        i = 1
        while i <= len(s):
            num_str = s[:i]
            if is_valid_ipaddr_num(num_str):
                if dots_left > 0:
                    buildIpAddr(accum + num_str + '.', s[i:], dots_left - 1)
                else:
                    buildIpAddr(accum + num_str, s[i:], -1)
            i += 1

    buildIpAddr('', s, 3)
    return res

def permuteUnique(nums: List[int]) -> List[List[int]]:
    """ leetcode #47 """

    res = []
    if len(nums) == 0:
        return res

    def buildPermutations(accum: List[int], taken_idx: set[int]):
        if len(accum) == len(nums):
            res.append(accum[:])
            return

        used_vals = set()
        for i in range(0, len(nums)):
            if i not in taken_idx and nums[i] not in used_vals:
                used_vals.add(nums[i])
                taken_idx.add(i)
                accum.append(nums[i])
                buildPermutations(accum, taken_idx)
                accum.pop()
                taken_idx.remove(i)

    buildPermutations([], set())
    return res

