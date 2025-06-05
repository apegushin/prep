import src.hash_map as hmlc
import pytest


@pytest.mark.parametrize('pattern, words, result',
                       [('abba', 'dog cat cat dog', True),
                        ('abba', 'dog cat cat fish', False),
                        ('aaaa', 'dog cat cat dog', False),])
def test_wordPattern(pattern, words, result):
    assert hmlc.wordPattern(pattern, words) == result

@pytest.mark.parametrize('s, t, result',
                       [('abcd', 'abcde', 'e'),
                        ('', 'y', 'y'),
                        ('abababab', 'babababab', 'b'),])
def test_findTheDifference(s, t, result):
    assert hmlc.findTheDifference(s, t) == result
