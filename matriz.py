linhas = 12
colunas = 12
s = 0

matriz = []
operacao = input()

for i in range(linhas):
    matriz.append([])
    for j in range(colunas):
        matriz[i].append(float(input()))

if operacao == 'S':
    for i in range(linhas):
        for j in range(colunas):
            if (j > i):
                soma += matriz[i][j]
                print(soma)
elif operacao == 'M':
    for i in range(linhas):
        for j in range(colunas):
            if (j > i):
                s = s+1
                soma += matriz[i][j]
                media = soma/s
                print(media)