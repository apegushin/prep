import src.prev_interviews as mcd
import pytest

@pytest.mark.parametrize('curwd, cdto, result',
                        [('/', 'foo', '/foo'),
                         ('/baz', '/bar', '/bar'),
                         ('/foo/bar', '../../../../..', '/'),
                         ('/x/y', '../p/../q', '/x/q'),
                         ('/x/y', '/p/./q', '/p/q'),
                        ])
def test_cd_dir(curwd, cdto, result):
    assert mcd.cd_dir(curwd, cdto) == result

@pytest.mark.parametrize('board, moves_list',
                        [([[0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 1, 0, 0, 1, 0],
                           [0, 0, 1, 0, 1, 1, 0],
                           [0, 0, 1, 0, 1, 0, 1],
                           [1, 1, 1, 0, 0, 0, 0]],
                           [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3),
                            (3, 3), (4, 3), (4, 4), (4, 5), (4, 6)]),
                        ])
def test_shortestBridge(board, moves_list):
    res = mcd.shortestPath(board)
    assert res == moves_list