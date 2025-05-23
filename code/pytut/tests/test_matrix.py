from src.matrix import MatrixLeetCode

class TestMatrixLeetCode:
    def setup_method(self, method):
        self.mlc = MatrixLeetCode()

    def test_spiralOrder(self):
        assert self.mlc.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
        assert self.mlc.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]