arquivoprodutos = open("c1_produtos.txt.", "r")
arquivovendas = open("c1_vendas.txt.", "r")

#leitura e inclusao na lista, tabela produtos

codprodutos = []
quant_estoque = []
quantMinima = []
totalvendido = []

for linha in arquivoprodutos:

    totalvendido.append(0)

    valores = linha.split(';')

    cod_s = valores[0]
    cod= int(cod_s)
    codprodutos.append (cod)

    quant_a = valores[1]
    quantA = int(quant_a)
    quant_estoque.append (quantA)

    quant_C = valores[2]
    quantCO = int(quant_C)
    quantMinima.append(quantA)

#leitura e inclusao na lista, tabela vendas
codvendas= []
quantidadevendida = []
sitvendas = []
canalvenda = []

for linha in arquivovendas:

    valoresvendas = linha.split(';')

    cod_a = valoresvendas[0]
    cod2= int(cod_a)
    codvendas.append (cod2)

    quant_v = valoresvendas[1]
    quantv = int(quant_v)
    quantidadevendida.append (quantv)

    sit_ = valoresvendas[2]
    sit = int(sit_)
    sitvendas.append(sit)

    canal_ = valoresvendas[3]
    canal = int(canal_)
    canalvenda.append(canal)


print("                         Atividade N2D - Estoque Operacional")
print("\nintegrantes do grupo: \nJuliana Marques \nTyago Wiesner \nLuis Augusto \nMatheus Costa \n")


contprod = 0
contvendas = 0
estoque_posvendas = []

while contvendas < len(codvendas):
    contprod = 0

    while contprod < len(codprodutos):
        situacao = sitvendas[contvendas]

        if codprodutos[contprod] == codvendas[contvendas] and (situacao == 100 or situacao == 102):
            totalvendido[contprod] = totalvendido[contprod] + quantidadevendida[contvendas]
            estoque_posvendas = totalvendido[contprod] - quant_estoque[contprod]
            necessidade = quantMinima - estoque_posvendas
            transferencia = necessidade
            if necessidade < 10:
                transferencia = 10

        contprod = contprod + 1
    contvendas = contvendas + 1

arquivocalc.write ("Produto    QtCO     QtMin     QtVendas      Estq.após Vendas      Necess.        Transf. de Arm p/ CO")

arquivocalc.write("{}    {}            {}       {}      {}        {}            {} \n ".format(codvendas, quant_estoque, totalvendido, estoque_posvendas, necessidade, transferencia))
print(quant_estoque)
print (estoque_posvendas)
print (codprodutos)
print (totalvendido)

arquivovendas.close()
arquivoprodutos.close()
            #relatorio de divergencias
contvendas = 0
arquivodivergencias= open("c1_divergencias.txt.","r")

while contvendas < len(sitvendas):

    situacao = sitvendas[contvendas]
    if situacao == 135:
        arquivodivergencias.write ("Linha {} – Venda cancelada".format(sitvendas.index(135)))
    elif situacao == 190:
        print(sitvendas.index(190))
        arquivodivergencias.write ("Linha {} – Venda não finalizada".format(sitvendas.index(190)))
    elif situacao == 999:
        print(sitvendas.index(999))
        arquivodivergencias.write("Linha {} –Erro desconhecido. Acionar equipe de TI".format(sitvendas.index(999)))
    elif codvendas != 16320 and  codvendas != 23400 and codvendas != 26440 and codvendas != 28790 and codvendas != 36540:
        arquivodivergencias.write("Linha { } –Código de Produto não encontrado {} ".format(sitvendas.index(cod), codvendas))

arquivodivergencia.close()

#Quantidades de Vendas por canal
arquivodicanal= open("c1_totcanal.txt.","r")

lista1 =[]
lista2 =[]
lista3 =[]
lista4 =[]

contvendas = 0
while contvendas < len(codvendas):
    contprod = 0
    while contprod < len(codprodutos):
        canal = canalvenda[contvendas]
        if canal == 1:
            lista1.append(totalvendido[contprod])
        elif canal == 2:
            lista2.append(totalvendido[contprod])
        elif canal == 3:
            lista3.append(totalvendido[contprod])
        elif canal == 4:
            lista4.append(totalvendido[contprod])

        contprod = contprod + 1
    contvendas = contvendas + 1

arquivodicanal.write ('Quantidades de Vendas por canal')
arquivodicanal.write ("1 -Representantes    {}\n".format(len(lista1)))
arquivodicanal.write ("2 – Website         {}\n".format(len(lista2)))
arquivodicanal.write ("3 – App móvel Android    {}\n".format(len(lista3)))
arquivodicanal.write ("4 – App móvel iPhone     {}\n".format(len(lista4)))