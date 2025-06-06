import src.bitwise as blc
import pytest

@pytest.mark.parametrize('divident, divisor, result',
                        [(10, 3, 3),
                         (10, 2, 5),
                         (10, -3, -3),
                         (10, -2, -5),
                         (2147483647, 2, 1073741823),
                         (-2147483648, 2, -1073741824),
                        ])
def test_addTwoNumbers(divident, divisor, result):
    assert blc.divide(divident, divisor) == result