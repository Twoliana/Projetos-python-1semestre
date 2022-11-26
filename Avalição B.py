#Gerador de senha

# w = write (escreve)
# r = read (ler)
# a - acrescent (acrescentar) 
# 27 = ;

def GeraSenha(Tipo, Tam):
    senha = ''
    i = 0
    while i < Tam:
        if Tipo == "A" or Tipo == "a":
            senha = senha + (random.choice(n))
        elif Tipo == "B" or Tipo == "b":
            senha = senha + (random.choice((a1 + a2)))
        elif Tipo == "C" or Tipo == "c":
            senha = senha + (random.choice(a2 + n))
        elif Tipo == "D" or Tipo == "d":
            senha = senha + (random.choice(a1 + a2 + n))
        elif Tipo == "E" or Tipo == "e":
            senha = senha + (random.choice(a1 + a2 + n + simb))
        i = i + 1
    return senha

import random
n = ['0','1','2','3','4','5','6','7','8','9']
a1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
simb = [']', '[', '}', '{', '(',')','*',"#",';','/','-','_','%',]


    #cabeçalho
print("                         Atividade N2B - Gerador de Senhas")
print("\nintegrantes do grupo: \nJuliana Marques \nTyago Wiesner \nLuis Augusto \nMatheus Costa")


Tipousuario = str(input('Digite o tipo de senha: '))
Tamusuario = int(input('Digite qual o tamanho da senha: '))

arquivosenhas = open('senhas.txt', 'w')
arquivomat = open('matr.txt','r')

matriculas = arquivomat.readline()
for matriculas in arquivomat:

    senha = GeraSenha(Tipousuario, Tamusuario)
    arquivosenhas.write(matriculas + ';' +senha)
    print (senha)
    #arquivosenhas.write(senha)

arquivosenhas.close()
arquivomat.close()





