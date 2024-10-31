start = 1
end = 100
acerto = False
while acerto == False:
    mid = (start + end)//2
    resposta = input(f'{mid} maior, menor ou igual?')
    resposta = resposta.lower()
    if resposta == 'igual':
        acerto = True
    elif resposta == 'menor':
        end = mid
    else:
        start = mid

if acerto == True:
    print('EU SABIA HAHAHAHA')