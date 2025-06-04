import src.strings as slc
import pytest

@pytest.mark.parametrize('s, l',
                        [('abcabcbb', 3),
                         ('bbbbb', 1),
                         ('pwwkew', 3),
                         ('', 0),
                        ])
def test_lengthOfLongestSubstring(s, l):
    assert slc.lengthOfLongestSubstring(s) == l

@pytest.mark.parametrize('s, pals',
                        [('babad', ['bab', 'aba']),
                         ('cbbd', ['bb']),
                         ('a', ['a']),
                        ])
def test_longestPalindrome(s, pals):
    if len(pals) == 1:
        assert slc.longestPalindrome(s) == pals[0]
    else:
        assert slc.longestPalindrome(s) in pals
