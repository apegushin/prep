def divide(dividend: int, divisor: int) -> int:
    """ leetcode #29 """

    MIN_INT = -1*(2**31)
    if divisor == 1: return dividend
    if dividend == MIN_INT and divisor == -1: return -MIN_INT-1

    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
    dividend = dividend if dividend < 0 else -dividend
    divisor = divisor if divisor < 0 else -divisor

    quotient = 0
    i, accum = 1, divisor

    while dividend <= accum and accum >= MIN_INT>>1:
        accum <<= 1
        i <<= 1

    while dividend <= divisor:
        if dividend <= accum:
            dividend -= accum
            quotient += i
        accum >>= 1
        i >>= 1

    return sign * quotient
