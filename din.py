#ler quantia de dinheiro e decompor em numero de notas e moedas
# sempre atualizar o din inicial para o resto q sobrou da divisao
d, c = map(int, input().split('.'))
print('NOTAS:')
cedulas = [100, 50, 20, 10, 5, 2]
for notas in cedulas:
    n = d//notas
    print(f'{int(n)} nota(s) de R$ {notas}.00')
    d = d%notas
print('MOEDAS:')
print(f'{int(d)} moeda(s) de R$ 1.00')
moedas = [50, 25, 10, 5, 1]
for cents in moedas:
    nc = c//cents
    print(f'{int(nc)} moeda(s) de R$ 0.{str(cents).zfill(2)}')
    c = c%cents