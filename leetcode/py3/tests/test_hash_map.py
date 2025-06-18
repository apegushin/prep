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

@pytest.mark.parametrize('numerator, denominator, result',
                        [(1, 2, '0.5'),
                         (2, 1, '2'),
                         (-4, 3, '-1.(3)'),
                         (-4, -1, '4'),
                         (5, 200, '0.025'),
                         (5, 2000, '0.0025'),
                         (5, 20000, '0.00025'),
                         (1, 500, '0.002'),
                         (-1, 500, '-0.002'),
                         (1, -500, '-0.002'),
                         (-1, -500, '0.002'),
                         (200, 5, '40'),
                         (1, 6, '0.1(6)'),
                         (-220, 5, '-44'),
                         (222, -5, '-44.4'),
                         (4, 333, '0.(012)'),
                        ])
def test_fractionToDecimal(numerator, denominator, result):
    assert hmlc.fractionToDecimal(numerator, denominator) == result

@pytest.mark.parametrize('sequence, result',
                        [('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT', ['CCCCCAAAAA', 'AAAAACCCCC']),
                         ('AAAAAAAAAAAAA', ['AAAAAAAAAA']),
                        ])
def test_findRepeatedDnaSequences(sequence, result):
    assert hmlc.findRepeatedDnaSequences(sequence).sort() == result.sort()

