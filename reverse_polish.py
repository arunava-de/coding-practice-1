import operator

def evaluate(tokens):

    S = []
    n = len(tokens)

    if n==1:
        return int(tokens[0])

    def divide(a, b):
        sign_a = -1 if a<0 else 1
        sign_b = -1 if b<0 else 1
        a = abs(a)
        b = abs(b)
        div = a//b 
        return div if sign_a==sign_b else -div

    ops = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : divide, 
    }

    for i in range(n):
        if tokens[i] in ops:
            b = S.pop()
            a = S.pop()
            res = ops[tokens[i]](int(a),int(b))

            S.append(res)
        else:
            S.append(tokens[i])

    return S[0]

tokens = ["2","1","+","3","*"]
evaluate(tokens)

tokens = ["4","13","5","/","+"]
evaluate(tokens)

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
evaluate(tokens)

tokens = ["12"]
evaluate(tokens)