import src.hash_map as hmlc
import pytest

@pytest.mark.parametrize('pattern, words, result',
                        [('abba', 'dog cat cat dog', True),
                         ('abba', 'dog cat cat fish', False),
                         ('aaaa', 'dog cat cat dog', False),
                        ])
def test_wordPattern(pattern, words, result):
    assert hmlc.wordPattern(pattern, words) == result

@pytest.mark.parametrize('s, t, result',
                        [('abcd', 'abcde', 'e'),
                         ('', 'y', 'y'),
                         ('abababab', 'babababab', 'b'),
                        ])
def test_findTheDifference(s, t, result):
    assert hmlc.findTheDifference(s, t) == result

@pytest.mark.parametrize('nums, result',
                        [([100,4,200,1,3,2], 4),
                         ([0,3,7,2,5,8,4,6,0,1], 9),
                         ([1,0,1,2], 3),
                        ])
def test_longestConsecutive(nums, result):
    assert hmlc.longestConsecutive(nums) == result
