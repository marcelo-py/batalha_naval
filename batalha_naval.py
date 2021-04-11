#por Marcelo Santos
matriz = dict()
quantlinha = int(input('Quantas linhas?: '))
quantcoluna = int(input('Quantas colunas?: '))
s = quantlinha + quantcoluna
for linha in range(0, quantlinha):
    matriz[linha] = []
    for c in range(0, quantcoluna):
        matriz[linha].append(['X'+ str(c)])
jogador1 = input('Nome do Jogador 1').upper()[0]
jogador2 = input('Nome do Jogador 2').upper()[0]

for m in matriz.items():
    print('\033[7;1;34m{}'.format(m[0], end=' '),end='')
    for l in m[1]:
        print('{}'.format(l),end='')
    print('\033[m')
cont = 0
while cont < s:
    joga = int(input('\033[1;32m{}\033[m =>joga em qual linha?'.format(jogador1)))
    while joga > len(matriz.keys()):
        print('Digite uma linha existente!')
        joga = int(input('\033[1;32m{}\033[m =>joga em qual linha?'.format(jogador1)))

    jogai = input('Qual indice? ').upper().replace('X', '')
    if jogai.isnumeric() or jogai.isalnum():
        jogai = int(jogai)

    while jogai >len(matriz[0]):
        print('Esse idice não existe! ')
        jogai = input('Qual indice? ').upper().replace('X', '')
        if jogai.isnumeric() or jogai.isalnum():
            jogai = int(jogai)

        #se ja jogaram, o codigo
    if 'X' not in matriz[joga][jogai][0]:
        print('Esse capo ja tem Soldado')
        continue
    matriz[joga][jogai] = [jogador1.center(2)]
    for m in matriz.items():
        print('\033[7;1;34m{}'.format(m[0], end=' '), end='')
        for l in m[1]:
            print('{}'.format(l), end='')
        print('\033[m')

    jogada2 = int(input('\033[1;32m{}\033[m =>joga em qual linha?'.format(jogador2)))
    while jogada2 > len(matriz.keys()):
        print('Digite uma linha existente!')
        jogada2 = int(input('\033[1;32m{}\033[m =>joga em qual linha?'.format(jogador2)))

    jogai2 = input('Qual indice? ').upper().replace('X', '')
    if jogai2.isnumeric() or jogai2.isalnum():
        jogai2 = int(jogai2)

    while jogai2 > len(matriz[0]):
        print('Esse idice não existe! ')
        jogai2 = input('Qual indice? ').upper().replace('X', '')
        if jogai2.isnumeric() or jogai2.isalnum():
            jogai2 = int(jogai2)


    while 'X' not in matriz[jogada2][jogai2][0]:
        print('Atenção! Campo com soldado')
        jogada2 = int(input('{} =>joga em qual linha?'.format(jogador2)))
        while jogada2 > len(matriz.keys()):
            print('Digite uma linha existente!')
            jogada2 = int(input('\033[1;32m{}\033[m =>joga em qual linha?'.format(jogador2)))

        jogai2 = input('Qual indice? ').upper().replace('X', '')
        if jogai2.isnumeric() or jogai2.isalnum():
            jogai2 = int(jogai2)

        while jogai2 > len(matriz[0]):
            print('Esse idice não existe! ')
            jogai2 = input('Qual indice? ').upper().replace('X', '')
            if jogai2.isnumeric() or jogai2.isalnum():
                jogai2 = int(jogai2)

    matriz[jogada2][jogai2] = [jogador2.center(2)]

    for m in matriz.items():
        print('\033[7;1;34m{}'.format(m[0], end=' '), end='')
        for l in m[1]:
            print('{}'.format(l), end='')
        print('\033[m')
    cont += 2
    print('-'*30)
print('\033[34mResultado final\033[m')
for m in matriz.items():
    print('\033[7;1;34m{}'.format(m[0], end=' '),end='')
    for l in m[1]:
        print('{}'.format(l),end='')
    print('\033[m')