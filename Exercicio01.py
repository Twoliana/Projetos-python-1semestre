cont = 1
A = []
POS = []
NEG = []

X = int(input('digite um valor:'))
if X >= 0 and X <= 50:

    while cont <= X:
        N = int(input('digite um valor:'))
        A.append(N)
        cont = cont + 1
        if N >= 0:
            POS.append(N)
        else:
            NEG.append(N)
else:
    print ("Valor digitado inválido")

print ("O total de números positivos digitados:", len(POS))
print ("O total de números negativos digitados:",len(NEG))
print ("O total de números digitados:",len(A))