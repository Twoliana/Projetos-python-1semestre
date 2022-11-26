# programa 08
L = []
R = []

LMin = int(input('Digite o menor valor:'))
LMax = int(input('Digite o maior valor:'))
if LMax > LMin:
        LMax = LMax
else:
    print ('O valor digitado é inapropriado. O valor Máximo deverá ser maior que o valor Mínimo.Logicamente.')
    LMax = int(input('Digite o maior valor:'))

cont = 1
A = int(input("Digite um valor para a lista:"))
while cont <= 10:
    if A > LMin and A < LMax:
        A = int(input("Digite um valor para a lista:"))
        L.append(A)
        cont = cont +1
    else:
        A = int(input("Digite um valor para a lista:"))
        R.append(A)
        cont = cont + 1

print (L)
print ("O tamanhdo a lista valida é", (len(L)))

print (R)
print ("Valores não invalidos", (len(L)))

