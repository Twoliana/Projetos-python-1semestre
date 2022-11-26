cont = 1
L = []

A = int(input('digite um valor:'))
if A >= 0 and A <= 50:

    while cont <= A:
        B = int(input('digite um valor:'))
        L.append(B)
        cont = cont + 1
else:
    print ("Valor digitado inválido")

for N in L:
    print (N)


from random import randint
z = randint (0,10)
print z