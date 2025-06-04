import pytest
import src.hash_map as hmlc

@pytest.mark.parametrize('pattern, words, result',
                       [('abba', 'dog cat cat dog', True),
                        ('abba', 'dog cat cat fish', False),
                        ('aaaa', 'dog cat cat dog', False),])
def test_wordPattern(pattern, words, result):
    assert hmlc.wordPattern(pattern, words) == result