# programa 07

N = int(input('digite um valor para a quantidade de itens da lista:'))
cont = 1
L = []
while cont <= N:
    X = int(input('digite um valor pra incluir na lista:'))
    L.append(X)
    cont = cont + 1

print (L)
print ("O tamanhdo a lista é", (len(L)))
