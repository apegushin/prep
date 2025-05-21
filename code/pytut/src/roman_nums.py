class RomanNumConverter:
    def intToRoman(self, num: int) -> str:
        def first_digit(num: int, dec_place: int = 1000) -> tuple[int, int]:
            if num == 0:
                return (0, 0)
            while dec_place >= 1:
                digit = num // dec_place
                if digit > 0:
                    return (digit, dec_place)
                else:
                    dec_place //= 10

        digit, dec_place = first_digit(num)
        dec2rom = {True: {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'},
                   False: {900: 'CM', 400: 'CD', 90: 'XC', 40: 'XL', 9: 'IX', 4: 'IV'}}
        res = ''
        while num > 0:
            check = digit != 4 and digit != 9
            for n in sorted(dec2rom[check].keys(), reverse = True):
                if n <= num:
                    res += dec2rom[check][n]
                    num -= n
                    break
            digit, dec_place = first_digit(num, dec_place)
        return res