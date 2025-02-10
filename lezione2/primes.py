from funzioni import is_n_prime

n=int(input("inserisci un numero"))

primes=[]

for i in range(2,n+1):
    if is_n_prime(i):
        primes.append(i)
print("i numeri primi entro",n,"sono",primes)