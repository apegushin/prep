from src.roman_nums import RomanNumConverterLeetCode

class TestRomanNumConverterLeetCode:
    def setup_method(self, method):
        print(f'setting up test for {method}')
        self.rnc = RomanNumConverterLeetCode()

    def teardown_method(self, method):
        print(f'tearing down after test for {method}')

    def test_intToRoman(self):
        print('test_roman_to_int')
        assert self.rnc.intToRoman(1) == 'I'
        assert self.rnc.intToRoman(3) == 'III'
        assert self.rnc.intToRoman(4) == 'IV'
        assert self.rnc.intToRoman(9) == 'IX'
        assert self.rnc.intToRoman(13) == 'XIII'
        assert self.rnc.intToRoman(58) == 'LVIII'
        assert self.rnc.intToRoman(1994) == 'MCMXCIV'
        assert self.rnc.intToRoman(3749) == 'MMMDCCXLIX'

    def test_romanToInt(self):
        assert self.rnc.romanToInt('III') == 3
        assert self.rnc.romanToInt('IV') == 4
        assert self.rnc.romanToInt('IX') == 9
        assert self.rnc.romanToInt('LVIII') == 58
        assert self.rnc.romanToInt('MCMXCIV') == 1994
        assert self.rnc.romanToInt('MMMCMXCIX') == 3999
        assert self.rnc.romanToInt('MMMCMXC') == 3990
        assert self.rnc.romanToInt('MMMDCCXLIX') == 3749