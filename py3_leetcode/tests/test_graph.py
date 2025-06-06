import src.graph as glc
import pytest

@pytest.mark.parametrize('numCourses, prereqs, decision',
                        [(2, [[1,0]], True),
                         (2, [[1,0],[0,1]], False),
                        ])
def test_canFinish(numCourses, prereqs, decision):
    assert glc.canFinish(numCourses, prereqs) == decision
