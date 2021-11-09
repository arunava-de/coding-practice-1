def is_match(s, p):
    if not p:
        return not s 

    first = bool(s) and p[0] in {s[0], '.'}

    if len(p)>=2 and p[1]=='*':
        return is_match(s, p[2:]) or first and is_match(s[1:], p)
    else:
        return first and is_match(s[1:], p[1:])
