from src.backtracking import BacktrackingLeetCode

class TestBacktrackingLeetCode:

    def setup_method(self, method):
        self.blc = BacktrackingLeetCode()

    def test_letterCombinations(self):
        assert self.blc.letterCombinations('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        assert self.blc.letterCombinations('2') == ['a', 'b', 'c']
        assert self.blc.letterCombinations('') == []

    def test_wordExists(self):
        assert self.blc.wordExists([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], 'ABCCED') == True
        assert self.blc.wordExists([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], 'SEE') == True
        assert self.blc.wordExists([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], 'ABCB') == False
        assert self.blc.wordExists([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS") == True