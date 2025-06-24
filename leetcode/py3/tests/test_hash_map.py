import src.hash_map as hmlc
import pytest

@pytest.mark.parametrize('pattern, words, result',
                        [('abba', 'dog cat cat dog', True),
                         ('abba', 'dog cat cat fish', False),
                         ('aaaa', 'dog cat cat dog', False),
                        ])
def test_word_pattern(pattern, words, result):
    assert hmlc.word_pattern(pattern, words) == result

@pytest.mark.parametrize('s, t, result',
                        [('abcd', 'abcde', 'e'),
                         ('', 'y', 'y'),
                         ('abababab', 'babababab', 'b'),
                        ])
def test_find_the_difference(s, t, result):
    assert hmlc.find_the_difference(s, t) == result

@pytest.mark.parametrize('nums, result',
                        [([100,4,200,1,3,2], 4),
                         ([0,3,7,2,5,8,4,6,0,1], 9),
                         ([1,0,1,2], 3),
                        ])
def test_longest_consecutive(nums, result):
    assert hmlc.longest_consecutive(nums) == result

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
def test_fraction_to_decimal(numerator, denominator, result):
    assert hmlc.fraction_to_decimal(numerator, denominator) == result

@pytest.mark.parametrize('sequence, result',
                        [('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT', ['CCCCCAAAAA', 'AAAAACCCCC']),
                         ('AAAAAAAAAAAAA', ['AAAAAAAAAA']),
                        ])
def test_find_repeated_dna_sequences(sequence, result):
    assert hmlc.find_repeated_dna_sequences(sequence).sort() == result.sort()

