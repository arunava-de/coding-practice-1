def fractionToDecimal(numerator: int, denominator: int) -> str:
    if numerator == 0: return "0"
    sign = bool(numerator > 0) ^ bool(denominator > 0)
    numerator, denominator = abs(numerator), abs(denominator)
    res = ("-" if sign else "") + str(numerator//denominator)
    remainder = numerator % denominator
    
    if remainder == 0: return res

    res += "."
    pos = {}
    while remainder != 0:
        if remainder not in pos:
            pos[remainder] = len(res)
        else:
            res = res[:pos[remainder]] + "(" + res[pos[remainder]:] + ")"
            return res
            
        res += str(remainder * 10 // denominator)
        remainder = (remainder * 10) % denominator
    
    return res