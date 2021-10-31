def divide(dividend: int, divisor: int) -> int:

    quotient = 0
    sign = None
    MAX = 2**31 - 1
    MIN = -2**31

    if dividend==0:
        return 0

    if divisor == 0 or (dividend == MIN and divisor == -1):
            return MAX

    if dividend*divisor<0:
        sign = -1
    else:
        sign = 1

    dividend = abs(dividend)
    divisor = abs(divisor)

    while dividend>=divisor:
        shift = 0
        while dividend>=(divisor<<shift):
            shift += 1

        quotient += 1<<(shift-1)
        
        dividend -= divisor<<(shift-1)

    return -quotient if sign==-1 else quotient

divide(10,3)