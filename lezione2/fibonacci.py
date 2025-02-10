from funzioni import fib
n=int(input("inserisci un numero:"))
numbers=[]
for i in range(1,n+1):
    numbers.append(fib(i))
print("i primi",n,"termini della successione di Fibonacci sono", numbers)

