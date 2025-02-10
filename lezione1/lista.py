numero=int(input("inserisci un numero"))
numeri_primi=[]
for i in range(2, numero+1):
    è_primo=True
    for j in range(2,i):
       if i%j==0:
             è_primo=False
    if è_primo:
        numeri_primi.append(i)
print("i numeri primi fino a", numero,"sono",numeri_primi)