class HashMapLeetCode:
    def wordPattern(self, pattern: str, s: str) -> bool:
        n = len(pattern)
        words = s.split(' ')
        if len(words) != n: return False

        c2word = {}
        words_set = set()
        for i in range(n):
            if pattern[i] not in c2word:
                if words[i] in words_set:
                    return False
                c2word[pattern[i]] = words[i]
                words_set.add(words[i])
            elif c2word[pattern[i]] != words[i]:
                return False
        return True