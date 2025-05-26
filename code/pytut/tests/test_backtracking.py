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

    def test_subsets(self):
        assert self.blc.subsets([1, 2, 3]).sort() == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]].sort()
        assert self.blc.subsets([0]).sort() == [[],[0]].sort()

    def test_combine(self):
        assert self.blc.combine(4, 2).sort() == [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]].sort()
        assert self.blc.combine(1, 1).sort() == [[1]].sort()
