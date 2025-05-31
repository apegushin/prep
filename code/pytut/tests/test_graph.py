import pytest
from src.graph import GraphLeetCode

class TestGraphLeetCode:

    def setup_method(self, method):
        self.glc = GraphLeetCode()

    @pytest.mark.parametrize("numCourses, prereqs, decision",
                             [(2, [[1,0]], True),
                              (2, [[1,0],[0,1]], False),
                             ])
    def test_canFinish(self, numCourses, prereqs, decision):
        assert self.glc.canFinish(numCourses, prereqs) == decision
