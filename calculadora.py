#calculadora rudimentar

print ("Escolha a operação desejada:")
escolha = int (input("[1]Soma\n[2]Subtração\n[3]Multiplicação\n[4]Divisão\n"))
while escolha > 4:
    print("Opção invalida, digite novamente!")
    escolha = int (input("[1]Soma\n[2]Subtração\n[3]Multiplicação\n[4]Divisão inteira\n"))
num1 = int (input("Digite o primeiro valor:\n"))
num2 = int (input("Digite o segundo valor:\n"))

if escolha == 1:
    soma = num1 + num2
    print(soma)
elif escolha == 2:
    sub = num1 - num2
    print (sub)
elif escolha ==3:
    mult== num1*num2
    print(mult)
else:
    if num1== 0:
        print("Os valores não podem ser nulos para esta operação.")
        num1 = int (input("Digite novamente o primeiro numero:\n"))
    elif num2== 0:
        print("Os valores não podem ser nulos para esta operação.")
        num2 = int (input("Digite novamente o segundo numero:\n"))
div = num1 / num2        
print (div)