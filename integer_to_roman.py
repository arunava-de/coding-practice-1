def int_to_roman(num):

    roman = ""
    num = str(num)
    n = len(num)
    c = n-1

    while c>=0:
        dig = int(num[n-c-1])
        if c==3:
            roman += 'M'*dig
        elif c==2:
            if dig==9:
                roman += "CM"
            elif dig>=5:
                roman += "D" + "C"*(dig-5)
            elif dig==4:
                roman += "CD"
            else:
                roman += "C"*dig 
        elif c==1:
            if dig==9:
                roman += "XC"
            elif dig>=5:
                roman += "L" + "X"*(dig-5)
            elif dig==4:
                roman += "XL"
            else:
                roman += "X"*dig
        else:
            if dig==9:
                roman += "IX"
            elif dig>=5:
                roman += "V" + "I"*(dig-5)
            elif dig==4:
                roman += "IV"
            else:
                roman += "I"*dig
        c -= 1

    return roman 

num = 332
        

    



