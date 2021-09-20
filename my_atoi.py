def myAtoi(s: str) -> int:
        
    solution = ''
    sign = None
    recording = False
    
    for char in s:
        # '+' '-'
        if ord(char) == 45 or ord(char) == 43:
            if recording: break
            if sign :return 0
            sign = int(char + '1')
            recording = True
            continue 
        # Space
        elif ord(char) == 32:
            if recording: break
            continue
        # Alpha
        elif ord(char) < 48 or ord(char) > 57:
            break
            
        solution += char
        recording = True

        
    # if positive and no sign
    sign = 1 if sign is None else sign 
    
    # if nothing recorded  0 
    solution = 0 if len(solution) == 0 else int(solution)*sign
    
    # Constraints
    solution = -2**31 if solution < -2**31 else solution
    solution = 2**31 -1 if solution > 2**31 -1 else solution
    
    return solution