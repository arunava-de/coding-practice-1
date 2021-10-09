def is_palindrome(s, e, string):

    while s<e:
        if string[s]==string[e]:
            s += 1
            e -= 1
        else:
            return False 
    return True

def partition(s):

    n = len(s)

    if n==1:
        return [[s]]

    result = []
    def recur(start, curr, s):
        nonlocal result
        if start>=len(s):
            result.append(curr[::])

        for end in range(start, len(s)):
            if is_palindrome(start, end, s):
                curr.append(s[start:end+1])
                recur(end+1, curr, s)
                curr.pop()


    recur(0, [], s)
    return result 


partition("aab")
