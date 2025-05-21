from src.roman_nums import RomanNumConverter

class TestRomanNumsLeetcodeProblems:
    def setup_method(self, method):
        print(f'setting up test for {method}')
        self.rnc = RomanNumConverter()

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