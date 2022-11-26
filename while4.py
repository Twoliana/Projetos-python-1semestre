N = int(input("Digite um número: "))
cont = 0
soma = 0
while cont < N:
    A = float(input("Digite um número: "))
    cont = cont +1
    if A > 0:
        soma += A
    
print ("O resultado da soma dos números positvos é", soma)
