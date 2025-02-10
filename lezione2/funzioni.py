def is_n_prime(x):
    for i in range(2,x):
        if x % i ==0:
            return False
    return True

def fattoriale(n):
    tot=1
    for i in range(1,n+1):
         tot= tot*i
    return tot

def fib(n):
    if n ==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

