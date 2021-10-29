import timeit

def my_pow_recur(x, n):
    if n==1:
        return x 

    return x*my_pow_recur(x, n-1)

def my_pow(x, n):
    return x**n

start = timeit.timeit()
my_pow_recur(123,10)
end = timeit.timeit()
print("Time for recursive:", end-start)

start = timeit.timeit()
my_pow(123,10)
end = timeit.timeit()
print("Time for normal:", end-start)

def my_pow(x, n):
    
    if n==0:
        return 1 

    pow = my_pow(x, n//2)

    if n%2==1:
        return x*pow*pow 
    else:
        return pow*pow

my_pow(2,10)
my_pow(-2,11)
my_pow(1/2,10)
my_pow(1/2,-10)
