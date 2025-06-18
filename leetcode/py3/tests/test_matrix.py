import src.matrix as mlc
import pytest

@pytest.mark.parametrize('matrix, spiral',
                        [([[1,2,3],
                           [4,5,6],
                           [7,8,9]], [1,2,3,6,9,8,7,4,5]),
                         ([[1,2,3,4],
                           [5,6,7,8],
                           [9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7]),
                        ])
def test_spiralOrder(matrix, spiral):
    assert mlc.spiralOrder(matrix) == spiral
    assert mlc.spiralOrderListPop(matrix) == spiral

@pytest.mark.parametrize('matrix, num_islands',
                        [([['1','1','0','0','0'],
                           ['1','1','0','0','0'],
                           ['0','0','1','0','0'],
                           ['0','0','0','1','1']], 3),
                        ])
def test_numIslands(matrix, num_islands):
    assert mlc.numIslands(matrix) == num_islands

@pytest.mark.parametrize('matrix, shortest_bridge',
                        [([[0, 1],
                           [1, 0]], 1),
                         ([[0, 1, 0],
                           [0, 0, 0],
                           [0, 0, 1]], 2),
                         ([[1, 1, 1, 1, 1],
                           [1, 0, 0, 0, 1],
                           [1, 0, 1, 0, 1],
                           [1, 0, 0, 0, 1],
                           [1, 1, 1, 1, 1]], 1),
                        ])
def test_shortestBridge(matrix, shortest_bridge):
    assert mlc.shortestBridge(matrix) == shortest_bridge