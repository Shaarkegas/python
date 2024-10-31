#1
def multi(x,y):
    originalx = x
    originaly = y
    produto = x
    if y == 0:
        return 0
    elif y == 1:
        return x
    y = abs(y)
    x = abs(x)
    for i in range(1,y):
        produto = produto + x
    if (originalx < 0) or (originaly < 0):
        produto = -produto
        return produto
    else:
        return produto
mult,plica = map(int,input('Escolha dois numeros para serem multiplcados: ').split())
print(f'a resposta é {multi(mult,plica)}')
#2
def expo(h,k):
    result = 1
    while k > 0:
        if k%2 == 1:
            result = multi(result,h)
        h = multi(h,h)
        k = k//2

    return result
exp,nente = map(int,input('Escolha um inteiro e um expoente: ').split())
print(f'a resposta é {expo(exp,nente)}')
#3
def div(l,d):
    if d == 0:
        print("O divisor não pode ser igual a zero.")
        exit()
    quociente = 0
    if (l > 0 and d > 0) or (l < 0 and d < 0):
        sinal = 1 
    elif (l>0 and d<0) or (l<0 and d>0):
        sinal = -1
    l = abs(l)
    d = abs(d)
    while l >= d:
        l -= d
        quociente += 1
    return multi(quociente,sinal)
divi,sao = map(int,input('Escolha um dividendo e um divisor: ').split())
print(f'a resposta é {div(divi,sao)}')
#4
def divresto(p,n):
    quo = div(p,n)
    resto = p - multi(quo,n)
    return resto
res,to = map(int,input('Escolha dois valores e veja o resto de sua divisao: ').split())
print(f'a resposta é {divresto(res,to)}')
#5
def crescimento(tempo):
    size = expo(2,tempo -1)
    final = multi(5,size)
    return final
anos = int(input('Insira uma certa quantia de tempo(em anos) e veja quantos CM a arvore crescerá: '))
print(crescimento(anos),'centimetros')
#6
def horas(segundos):
    hr = div(segundos,3600)
    segundos = divresto(segundos,3600)
    minu = div(segundos,60)
    seg = divresto(segundos,60)
    return(hr,minu,seg)
segs = int(input('Insira uma certa quantia de tempo(em segundos) e veja quantas horas, minutos e segundos é equivalente: '))
print(f'hr:min:sg = {horas(segs)}')