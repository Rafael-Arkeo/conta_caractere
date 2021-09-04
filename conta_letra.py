""""Programa para contar quantas vezes determinada string foi digitada
    pelo usuário.

    Inspirado pelo exercício passado no curso de ADS na disciplina intruduçao a progra
    mação em C,que fazia basicamente a mesma coisa porém se limitava a contar
    somente as entradas (a,e,i,o,u) usando swtch case para isso.
    Mas e se eu quiser guardar e contar todas as entradas digitadas pelo usuário
    e depois exibir o resultado no final.É quase impóssivel o uso de ifs para cada entrada!

    Segue abaixo como resolvi o problema
"""
#####################################################################################################

""""Criei uma matriz para armazenar dois valores:matriz[0] para a entrada do usuário
    e matriz[1] para contar o número de vezes que foi digitada aquela cadeia de strings"""

matriz = [
    [],
    []
]

"""Depois criei uma estrutura de repetição while true,pare que  o programa se repita 
    equanto o usuário não digitar o caractere ponto. linha 59 """


def procura_vetor(matriz, string, d, c):
    """"Função para descobrir qual é a posição da string na matriz[0]
        e então adcionar mais 1 na matriz[1] na posição relacionada
        com ela"""
    if matriz[d][c] == string:
        matriz[d + 1][c] += 1
        return matriz[d + 1][c]
    else:

        return procura_vetor(matriz, string, d, c+1)


def cria_e_conta_letras(matriz, string, d):
    """Funçao para verificar se a string já existe
        na lista.Se já houver ela roda a função procura_vetor
        se não houver ela usa a funçao append e adciona a string a lista
        e o valor +1 na lista a ela relacionada"""
    a = 0
    b = 0

    if string in matriz[d]:
        procura_vetor(matriz, letra, a, b)


    else:
        matriz[d].append(string)
        matriz[d + 1].append(1)


while True:
    letra = input('digite uma letra:')
    if letra == '.':
        break
    cria_e_conta_letras(matriz, letra, 0)



r = 0
for i in matriz[0]:
    """"funçao para mostrar os carecteres mas o nuḿeros de vezes 
        que ele foi digitado"""
    if matriz[1][r] == 1:
        print(f'O carctere ->{matriz[0][r]}<- foi digitado {matriz[1][r]} vez')

        r += 1

    else:
        print(f'O carctere ->{matriz[0][r]}<- foi digitado {matriz[1][r]} vezes')



        r += 1

