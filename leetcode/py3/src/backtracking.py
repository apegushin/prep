from typing import List

def letter_combinations(digits: str) -> list[str]:
    """ leetcode #17 """

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

    def add_letter(i, s):
        if i != len(digits):
            for c in dig2let[digits[i]]:
                add_letter(i + 1, s + c)
        else:
            res.append(s)
            return

    add_letter(0, '')
    return res

def word_exists(board: list[list[str]], word: str) -> bool:
    """ leetcode #79 """

    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    def char_found(i, j, n) -> bool:
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) \
            or visited[i][j] or board[i][j] != word[n]:
            return False

        if n == len(word) - 1:
            return True
        else:
            visited[i][j] = True
            res = char_found(i + 1, j, n + 1) \
                or char_found(i - 1, j, n + 1) \
                or char_found(i, j + 1, n + 1) \
                or char_found(i, j - 1, n + 1)
            visited[i][j] = False
            return res

    for i in range(len(board)):
        for j in range(len(board[i])):
            if char_found(i, j, 0):
                return True

    return False

def subsets(nums: List[int]) -> List[List[int]]:
    """ leetcode #78 """

    res = []

    def add_subset(cur_s, i):
        if i == len(nums):
            res.append(cur_s[:])
            return

        cur_s.append(nums[i])
        add_subset(cur_s, i + 1)
        cur_s.pop()
        add_subset(cur_s, i + 1)

    add_subset([], 0)
    return res

def subsets_generator(nums: List[int]):
    """ leetcode #78 implemented as generator """

    def add_subset(cur_s, i):
        if i == len(nums):
            yield cur_s[:]

        else:
            cur_s.append(nums[i])
            yield from add_subset(cur_s, i + 1)
            cur_s.pop()
            yield from add_subset(cur_s, i + 1)

    yield from add_subset([], 0)

def combine(n: int, k: int) -> List[List[int]]:
    """ leetcode #77 """

    res = []

    def build_combination(c, i):
        if len(c) == k:
            res.append(c[:])
            return

        for j in range(i, n + 1):
            build_combination(c + [j], j + 1)

    build_combination([], 1)
    return res

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """ leetcode #39 """

    res = []
    candidates.sort()

    def find_comb(comb, idx):
        sc = sum(comb)
        if sc == target:
            res.append(comb[:])
            return

        for i in range(idx, len(candidates)):
            if sc + candidates[i] > target:
                break
            find_comb(comb + [candidates[i]], i)

    find_comb([], 0)
    return res

def word_break(s: str, word_dict: List[str]) -> bool:
    """ leetcode #139 """

    if len(s) == 0: return False

    word_set = set(word_dict)
    words = []
    def break_words(s: str) -> bool:
        if s == '':
            return True
        for i in range(1, len(s) + 1):
            if s[0:i] in word_set:
                words.append(s[0:i])
                if break_words(s[i:]):
                    return True
                words.pop()
        return False

    return break_words(s)

def restore_ip_addresses_naive(s: str) -> List[str]:
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

    def build_ip_addr(pos: int, dots_left: int):
        if dots_left == 0 and pos == len(s) and is_valid_ip():
            res.append(''.join(accum))
            return

        if dots_left > 0 and len(accum) > 0 and accum[-1] != '.':
            accum.append('.')
            build_ip_addr(pos, dots_left - 1)
            accum.pop()

        if pos < len(s):
            accum.append(s[pos])
            build_ip_addr(pos + 1, dots_left)
            accum.pop()

    build_ip_addr(0, 3)
    return res

def restore_ip_addresses(s: str) -> List[str]:
    """ leetcode #93 """

    res = []
    if len(s) < 4 or len(s) > 12:
        return res

    def is_valid_ipaddr_num(num_str: str) -> bool:
        return not (len(num_str) == 0 or len(num_str) > 3
            or (num_str[0] == '0' and len(num_str) > 1)
            or (int(num_str) > 255))

    def build_ip_addr(accum: str, s: str, dots_left: int):
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
                    build_ip_addr(accum + num_str + '.', s[i:], dots_left - 1)
                else:
                    build_ip_addr(accum + num_str, s[i:], -1)
            i += 1

    build_ip_addr('', s, 3)
    return res

def permute_unique(nums: List[int]) -> List[List[int]]:
    """ leetcode #47 """

    res = []
    if len(nums) == 0:
        return res

    def build_permutations(accum: List[int], taken_idx: set[int]):
        if len(accum) == len(nums):
            res.append(accum[:])
            return

        used_vals = set()
        for i in range(0, len(nums)):
            if i not in taken_idx and nums[i] not in used_vals:
                used_vals.add(nums[i])
                taken_idx.add(i)
                accum.append(nums[i])
                build_permutations(accum, taken_idx)
                accum.pop()
                taken_idx.remove(i)

    build_permutations([], set())
    return res

