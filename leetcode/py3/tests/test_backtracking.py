import src.backtracking as blc
import pytest


@pytest.mark.parametrize('digits, result',
                         [('23', ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']),
                          ('2', ['a', 'b', 'c']),
                          ('', [])
                          ])
def test_letter_combinations(digits, result):
    assert blc.letter_combinations(digits) == result


@pytest.mark.parametrize('board, word, result',
                         [([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED', True),
                          ([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'SEE', True),
                          ([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCB', False),
                          ([['A', 'B', 'C', 'E'], ['S', 'F', 'E', 'S'], ['A', 'D', 'E', 'E']], 'ABCESEEEFS', True),
                          ])
def test_word_exists(board, word, result):
    assert blc.word_exists(board, word) == result


@pytest.mark.parametrize('nums, subsets',
                         [([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
                          ([0], [[], [0]]),
                          ])
def test_subsets(nums, subsets):
    assert blc.subsets(nums).sort() == subsets.sort()


@pytest.mark.parametrize('n, k, combinations',
                         [(4, 2, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
                          (1, 1, [[1]]),
                          ])
def test_combine(n, k, combinations):
    assert blc.combine(n, k).sort() == combinations.sort()


@pytest.mark.parametrize('candidates, target, combinations',
                         [([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
                          ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
                          ([2], 1, []),
                          ([2, 3, 9], 11, [[2, 2, 2, 2, 3], [2, 3, 3, 3], [2, 9]]),
                          ])
def test_combination_sum(candidates, target, combinations):
    assert blc.combination_sum(candidates, target).sort() == combinations.sort()


@pytest.mark.parametrize('s, wordDict, result',
                         [('leetcode', ['leet', 'code'], True),
                          ('applepenapple', ['apple', 'pen'], True),
                          ('catsandog', ['cats', 'dog', 'sand', 'and', 'cat'], False),
                          ])
def test_word_break(s, wordDict, result):
    assert blc.word_break(s, wordDict) == result


@pytest.mark.parametrize('s, result',
                         [('25525511135', ["255.255.11.135", "255.255.111.35"]),
                          ('0000', ["0.0.0.0"]),
                          ('101023', ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]),
                          ])
def test_restore_ip_addresses(s, result):
    assert blc.restore_ip_addresses(s) == result


@pytest.mark.parametrize('nums, permutations',
                         [([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
                          ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
                          ])
def test_permute_unique(nums, permutations):
    assert blc.permute_unique(nums) == permutations
