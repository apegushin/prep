import src.linked_lists as lllc
import pytest

@pytest.mark.parametrize('list1, list2, result',
                        [([2,4,3], [5,6,4], [8, 0, 7]),
                        ])
def test_addTwoNumbers(list1, list2, result):
    h1 = lllc.createFromList(list1)
    h2 = lllc.createFromList(list2)
    h3 = lllc.addTwoNumbers(h1, h2)
    l3 = lllc.linkedList2List(h3)
    l3.reverse()
    assert l3 == result

@pytest.mark.parametrize('list1, remove, result',
                        [([1,2,6,3,4,5,6], 6, [1,2,3,4,5]),
                         ([1,2,6,3,4,5,6], 3, [1,2,6,4,5,6]),
                         ([], 3, []),
                         ([1,2], 3, [1,2]),
                         ([2], 2, []),
                         ([1, 2], 2, [1]),
                         ([2, 1], 2, [1]),
                        ])
def test_removeElements(list1, remove, result):
    h1 = lllc.createFromList(list1)
    h2 = lllc.removeElements(h1, remove)
    assert lllc.linkedList2List(h2) == result

@pytest.mark.parametrize('list, left, right, result',
                        [([1,2,3,4,5], 2, 4, [1,4,3,2,5]),
                         ([1,2,3], 1, 1, [1,2,3]),
                         ([1,2,3], 1, 2, [2,1,3]),
                         ([1,2,3], 2, 2, [1,2,3]),
                         ([1,2,3], 1, 3, [3,2,1]),
                         ([1,2,3,4,5], 1, 5, [5,4,3,2,1]),
                        ])
def test_reverseBetween(list, left, right, result):
    h1 = lllc.createFromList(list)
    h2 = lllc.reverseBetween(h1, left, right)
    assert lllc.linkedList2List(h2) == result

@pytest.mark.parametrize('list, reverse_list',
                        [([], []),
                         ([1], [1]),
                         ([1,2], [2,1]),
                         ([1,2,3], [3,2,1]),
                         ([1,2,3,1], [1,3,2,1]),
                         ([1,2,3,4,5], [5,4,3,2,1]),
                        ])
def test_reverse(list, reverse_list):
    h1 = lllc.createFromList(list)
    h2 = lllc.reverseList(h1)
    l2 = lllc.linkedList2List(h2)
    assert l2 == reverse_list

@pytest.mark.parametrize('list1, list2, list3, list4, result',
                        [([], [], [], [], []),
                         ([1], [1], [], [1], [1,1,1]),
                         ([], [1], [1], [], [1,1]),
                         ([1,2], [3,4], [5,6], [7,8], [1,2,3,4,5,6,7,8]),
                         ([1,2,3], [1,2,3], [1,2,3], [1,2,3], [1,1,1,1,2,2,2,2,3,3,3,3]),
                         ([1,2], [1,2,3], [2,3,4], [1,2,3,4,5,6], [1,1,1,2,2,2,2,3,3,3,4,4,5,6]),
                        ])
def test_mergeKLists(list1, list2, list3, list4, result):
    h1 = lllc.createFromList(list1)
    h2 = lllc.createFromList(list2)
    h3 = lllc.createFromList(list3)
    h4 = lllc.createFromList(list4)
    hr = lllc.mergeKLists([h1, h2, h3, h4])
    assert lllc.linkedList2List(hr) == result

@pytest.mark.parametrize('list, swapped',
                        [([], []),
                         ([1], [1]),
                         ([1,2], [2,1]),
                         ([1,2,3], [2,1,3]),
                         ([1,2,3,4],[2,1,4,3]),
                         ([1,2,3,4,5,6], [2,1,4,3,6,5]),
                         ([1,2,3,4,5,6,7,8,9], [2,1,4,3,6,5,8,7,9]),
                        ])
def test_swapPairs(list, swapped):
    h1 = lllc.createFromList(list)
    h2 = lllc.swapPairs(h1)
    assert lllc.linkedList2List(h2) == swapped

