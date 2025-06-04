from src.strings import StringLeetCode

class TestStringLeetcode:

    def setup_method(self, method):
        print(f'setting up test for {method}')
        self.slp = StringLeetCode()

    def teardown_method(self, method):
        print(f'tearing down after test for {method}')

    def test_lengthOfLongestSubstring(self):
        assert self.slp.lengthOfLongestSubstring('abcabcbb') == 3
        assert self.slp.lengthOfLongestSubstring('bbbbb') == 1
        assert self.slp.lengthOfLongestSubstring('pwwkew') == 3
        assert self.slp.lengthOfLongestSubstring('') == 0

    def test_longestPalindrome(self):
        assert self.slp.longestPalindrome('babad') == 'bab' or self.slp.longestPalindrome('babad') == 'aba'
        assert self.slp.longestPalindrome('cbbd') == 'bb'
        assert self.slp.longestPalindrome('a') == 'a'
