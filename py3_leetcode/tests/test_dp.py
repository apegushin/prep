import src.dp as dplc
import pytest

@pytest.mark.parametrize('coins, amount, result',
                        [([1,2,5], 11, 3),
                         ([2], 3, -1),
                         ([1], 0, 0),
                         ([1,2,5], 11, 3),
                         ([2], 3, -1),
                         ([1], 0, 0),
                        ])
def test_coinChange(coins, amount, result):
    assert dplc.coinChange_recursive(coins, amount) == result

@pytest.mark.parametrize('n, result',
                        [(2, 2),
                         (3, 3),
                         (4, 5),
                        ])
def test_climbStairs(n, result):
    assert dplc.climbStairs(n) == result

@pytest.mark.parametrize('nums, result',
                        [([1,2,3,1], 4),
                         ([2,7,9,3,1], 12),
                        ])
def test_rob(nums, result):
    assert dplc.rob(nums) == result

@pytest.mark.parametrize('s, wordDict, result',
                        [('leetcode', ['leet','code'], True),
                         ('applepenapple', ['apple','pen'], True),
                         ('catsandog', ['cats','dog','sand','and','cat'], False),
                        ])
def test_wordBreak(s, wordDict, result):
    assert dplc.wordBreak(s, wordDict) == result