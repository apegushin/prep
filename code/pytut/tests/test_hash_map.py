import pytest
from src.hash_map import HashMapLeetCode

class TestHashMapLeetCode:

    def setup_method(self, method):
        self.hmlc = HashMapLeetCode()

    @pytest.mark.parametrize('pattern, words, result',
                             [('abba', 'dog cat cat dog', True),
                              ('abba', 'dog cat cat fish', False),
                              ('aaaa', 'dog cat cat dog', False),])
    def test_wordPattern(self, pattern, words, result):
        assert self.hmlc.wordPattern(pattern, words) == result