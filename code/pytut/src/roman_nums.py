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

    def romanToInt(self, s: str) -> int:
        res: int = 0
        i: int = 0
        sn = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        while i < len(s):
            if i + 1 < len(s) and s[i: i + 2] in sn.keys():
                res += sn[s[i:i+2]]
                i += 2
            else:
                res += n[s[i]]
                i += 1
        return res
