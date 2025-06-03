import pytest
from src.bitwise import BitwiseLeetCode

class TestBitwiseLeetCode:

    def setup_method(self, method):
        self.blc = BitwiseLeetCode()

    @pytest.mark.parametrize("divident, divisor, result",
                             [(10, 3, 3),
                              (10, 2, 5),
                              (10, -3, -3),
                              (10, -2, -5),
                              (2147483647, 2, 1073741823),
                              (-2147483648, 2, -1073741824),])
    def test_addTwoNumbers(self, divident, divisor, result):
        assert self.blc.divide(divident, divisor) == result