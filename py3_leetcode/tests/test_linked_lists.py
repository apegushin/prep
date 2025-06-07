import src.linked_lists as lllc
import pytest

@pytest.mark.parametrize('l1, l2, result',
                        [([2,4,3], [5,6,4], [8, 0, 7]),
                        ])
def test_addTwoNumbers(l1, l2, result):
    h1 = lllc.createFromList(l1)
    h2 = lllc.createFromList(l2)
    h3 = lllc.addTwoNumbers(h1, h2)
    l3 = lllc.linkedList2List(h3)
    l3.reverse()
    assert l3 == result

@pytest.mark.parametrize('l1, remove, result',
                        [([1,2,6,3,4,5,6], 6, [1,2,3,4,5]),
                         ([1,2,6,3,4,5,6], 3, [1,2,6,4,5,6]),
                         ([], 3, []),
                         ([1,2], 3, [1,2]),
                         ([2], 2, []),
                         ([1, 2], 2, [1]),
                         ([2, 1], 2, [1]),
                        ])
def test_removeElements(l1, remove, result):
    h1 = lllc.createFromList(l1)
    h2 = lllc.removeElements(h1, remove)
    assert lllc.linkedList2List(h2) == result

@pytest.mark.parametrize('l, left, right, result',
                        [([1,2,3,4,5], 2, 4, [1,4,3,2,5]),
                         ([1,2,3], 1, 1, [1,2,3]),
                         ([1,2,3], 1, 2, [2,1,3]),
                         ([1,2,3], 2, 2, [1,2,3]),
                         ([1,2,3], 1, 3, [3,2,1]),
                         ([1,2,3,4,5], 1, 5, [5,4,3,2,1]),
                        ])
def test_reverseBetween(l, left, right, result):
    h1 = lllc.createFromList(l)
    h2 = lllc.reverseBetween(h1, left, right)
    assert lllc.linkedList2List(h2) == result

@pytest.mark.parametrize('l, reverse_list',
                        [([], []),
                         ([1], [1]),
                         ([1,2], [2,1]),
                         ([1,2,3], [3,2,1]),
                         ([1,2,3,1], [1,3,2,1]),
                         ([1,2,3,4,5], [5,4,3,2,1]),
                        ])
def test_reverse(l, reverse_list):
    h1 = lllc.createFromList(l)
    h2 = lllc.reverseList(h1)
    l2 = lllc.linkedList2List(h2)
    assert l2 == reverse_list

@pytest.mark.parametrize('l1, l2, l3, l4, result',
                        [([], [], [], [], []),
                         ([1], [1], [], [1], [1,1,1]),
                         ([], [1], [1], [], [1,1]),
                         ([1,2], [3,4], [5,6], [7,8], [1,2,3,4,5,6,7,8]),
                         ([1,2,3], [1,2,3], [1,2,3], [1,2,3], [1,1,1,1,2,2,2,2,3,3,3,3]),
                         ([1,2], [1,2,3], [2,3,4], [1,2,3,4,5,6], [1,1,1,2,2,2,2,3,3,3,4,4,5,6]),
                        ])
def test_mergeKLists(l1, l2, l3, l4, result):
    h1 = lllc.createFromList(l1)
    h2 = lllc.createFromList(l2)
    h3 = lllc.createFromList(l3)
    h4 = lllc.createFromList(l4)
    hr = lllc.mergeKLists([h1, h2, h3, h4])
    assert lllc.linkedList2List(hr) == result

@pytest.mark.parametrize('l, swapped',
                        [([], []),
                         ([1], [1]),
                         ([1,2], [2,1]),
                         ([1,2,3], [2,1,3]),
                         ([1,2,3,4],[2,1,4,3]),
                         ([1,2,3,4,5,6], [2,1,4,3,6,5]),
                         ([1,2,3,4,5,6,7,8,9], [2,1,4,3,6,5,8,7,9]),
                        ])
def test_swapPairs(l, swapped):
    h1 = lllc.createFromList(l)
    h2 = lllc.swapPairs(h1)
    assert lllc.linkedList2List(h2) == swapped

@pytest.mark.parametrize('l, sorted',
                        [([-1,5,3,4,0], [-1,0,3,4,5]),
                         ([], []),
                         ([4,2,1,3], [1,2,3,4]),
                        ])
def test_sortList(l, sorted):
    h1 = lllc.createFromList(l)
    h2 = lllc.sortList(h1)
    assert lllc.linkedList2List(h2) == sorted
