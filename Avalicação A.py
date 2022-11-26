arquivo = open("vendas.txt", "r")

listacod = []
listaquant = []
listaval = []
listageral = []


#criação de listas com os dados dos arquivos
for linha in arquivo:

    valores = linha.split(';')

    cod_s = valores[0]
    cod= int(cod_s)
    listacod.append (cod)

    quant_s = valores[1]
    quant = int(quant_s)
    listaquant.append (quant)

    valor_s = valores[2]
    valor = float(valor_s)
    listaval.append (valor)

arquivo.close()

#cabeçalho
print("                         Atividade NA2 - Totalização simples de vendas de produtos")
print("\nintegrantes do grupo: \nJuliana Marques \nTyago Wiesner \nLuis Augusto \nMatheus Costa")

#usuario digita o codigo do produto
pesquisador = int(input("\nDigite o codigo do produto:"))

while pesquisador!= 0:
    while pesquisador < 10000 or pesquisador > 21000 and pesquisador != 0:
        print(pesquisador, "Valor inválido. Precisa ser entre 10000 e 21000")
        pesquisador = int(input("\nDigite o codigo do produto:"))

    #usar o valor digitado e localizar seu indice dentro da lista, logo após buscar quantidade e valor(usando o indice da variavel cod)

    listavendasgeral = []
    i = 0
    Achei = False

    while i < 1000:
        if listacod[i] == pesquisador:
            Achei = True
            quantp = listaquant[i]
            valorp = listaval[i]
            totalvendas = quantp * valorp
            listavendasgeral.append(totalvendas)

        i = i + 1

#soma dos resultados de cada linha de venda e quantidade de produto.
    totalimpresso = (sum(listavendasgeral))
    print ('Total vendido do produto {} = R$ {:.2f}'.format(pesquisador,totalimpresso))
    pesquisador = int(input("\nDigite o codigo do produto:"))

print("Fim do programa")