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
    print(m[0], end=' ')
    for l in m[1]:
        print('{}'.format(l),end='')
    print()
cont = 0
while cont < s:
    joga = int(input('{} =>joga em qual linha?'.format(jogador1)))
    while joga > len(matriz.keys()):
        print('Digite uma linha existente!')
        joga = int(input('{} =>joga em qual linha?'.format(jogador1)))

    jogai = input('Qual indice? ').upper().replace('X', '')
    if jogai.isnumeric() or jogai.isalnum():
        jogai = int(jogai)

    while jogai >len(matriz[0]):
        print('Esse idice não existe! ')
        jogai = input('Qual indice? ').upper().replace('X', '')
        if jogai.isnumeric() or jogai.isalnum():
            jogai = int(jogai)

    matriz[joga][jogai] = [jogador1.center(2)]
    print(type(matriz[joga][jogai]))
    for m in matriz.items():
        print(m[0], end=' ')
        for l in m[1]:
            print('{}'.format(l), end='')
        print()


    jogada2 = int(input('{} =>joga em qual linha?'.format(jogador2)))
    while jogada2 > len(matriz.keys()):
        print('Digite uma linha existente!')
        jogada2 = int(input('{} =>joga em qual linha?'.format(jogador2)))

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
        print(m[0], end=' ')
        for l in m[1]:
            print('{}'.format(l), end='')
        print()
    cont += 1
    print('-'*30)
    print(matriz)

for m in matriz.items():
    print(m[0], end=' ')
    for l in m[1]:
        print('{}'.format(l),end='')
    print()


