estados = []
alfabeto = []
transicoes = {}
e_inicial = 1
e_final =2

while True:
    estado = input('Informe um estado')
    if(estado == ''):
        break
    estados.append(estado)

while True:
    termos_alfa = input('Informe um catacter')
    if(termos_alfa == ''):
        break
    alfabeto.append(termos_alfa)

for estado in estados:
    transicoes_local = {}
    for termos_alfa in alfabeto:
        transicao = input({f'{estado}{termos_alfa}='})
        transicoes_local[termos_alfa] = estado
    transicoes[estado] = transicoes_local



print(estados)
print(alfabeto)

