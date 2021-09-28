def reverse(s):
    n = len(s)
    if n==1:
        return 

    for i in range(n//2):
        s[i], s[n-i-1] = s[n-i-1], s[i]

s = list("abdabd")
reverse(s)
print(s)
