def divide(dividend: int, divisor: int) -> int:

    quotient = 0
    sign = None

    if dividend==0:
        return 0


    if dividend*divisor<0:
        sign = -1
    else:
        sign = 1

    dividend = abs(dividend)
    divisor = abs(divisor)

    if dividend<divisor:
        return 0

    while dividend>0:
        if dividend<divisor:
            break
        dividend = dividend - divisor
        quotient += 1

    quotient = sign*quotient

    if quotient<-2**31:
        return -2**31
    elif quotient>(2**31)-1:
        return (2**31)-1

    return quotient

divide(9,3)
divide(-10,3)
divide(7,-3)
divide(1,1)