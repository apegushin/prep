class StringLeetCode:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        maxlen = 1
        i, j = 0, 1
        track = {s[0]: 0}
        while j < len(s):
            if s[j] not in track.keys() or track[s[j]] < i:
                track[s[j]] = j
                maxlen = max(maxlen, j - i + 1)
            else:
                i = track[s[j]] + 1
                track[s[j]] = j
            j += 1
        return maxlen

    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        def longestPalindromeFromCenter(i: int, j: int, s: str) -> str:
            res = ''
            while i >= 0 and j < len(s) and s[i] == s[j]:
                res = s[i:j+1]
                i -= 1
                j += 1
            return res

        maxPal = ''
        for i in range(0, len(s) - 1):
            res = longestPalindromeFromCenter(i, i, s)
            maxPal = res if len(res) > len(maxPal) else maxPal
            res = longestPalindromeFromCenter(i, i + 1, s)
            maxPal = res if len(res) > len(maxPal) else maxPal
        return maxPal

