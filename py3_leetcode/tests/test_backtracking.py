import src.backtracking as blc

def test_letterCombinations():
    assert blc.letterCombinations('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    assert blc.letterCombinations('2') == ['a', 'b', 'c']
    assert blc.letterCombinations('') == []

def test_wordExists():
    assert blc.wordExists([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], 'ABCCED') == True
    assert blc.wordExists([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], 'SEE') == True
    assert blc.wordExists([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], 'ABCB') == False
    assert blc.wordExists([['A','B','C','E'],['S','F','E','S'],['A','D','E','E']], 'ABCESEEEFS') == True

def test_subsets():
    assert blc.subsets([1, 2, 3]).sort() == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]].sort()
    assert blc.subsets([0]).sort() == [[],[0]].sort()

def test_combine():
    assert blc.combine(4, 2).sort() == [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]].sort()
    assert blc.combine(1, 1).sort() == [[1]].sort()

def test_combinationSum():
    assert blc.combinationSum([2,3,6,7], 7).sort() == [[2,2,3],[7]].sort()
    assert blc.combinationSum([2,3,5], 8).sort() == [[2,2,2,2],[2,3,3],[3,5]].sort()
    assert blc.combinationSum([2], 1) == []
    assert blc.combinationSum([2, 3, 9], 11).sort() == [[2, 2, 2, 2, 3], [2, 3, 3, 3], [2, 9]].sort()
