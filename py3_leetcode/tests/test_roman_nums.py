import pytest
import src.roman_nums as rnlc

@pytest.mark.parametrize('integer, roman',
                        [(1, 'I'),
                         (3, 'III'),
                         (4, 'IV'),
                         (9, 'IX'),
                         (13, 'XIII'),
                         (58, 'LVIII'),
                         (1994, 'MCMXCIV'),
                         (3749, 'MMMDCCXLIX'),
                        ])
def test_intToRoman(integer, roman):
    assert rnlc.intToRoman(integer) == roman

@pytest.mark.parametrize('roman, integer',
                        [('III', 3),
                         ('IV', 4),
                         ('IX', 9),
                         ('LVIII', 58),
                         ('MCMXCIV', 1994),
                         ('MMMCMXCIX', 3999),
                         ('MMMCMXC', 3990),
                         ('MMMDCCXLIX', 3749),
                        ])
def test_romanToInt(roman, integer):
    assert rnlc.romanToInt(roman) == integer
