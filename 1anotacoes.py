# "%.xf" pra determinar quantos numeros após o ponto
 "%.3f" % x --> x.xxx

#float = numeros com casas decimais
#int = numeros inteiros

input() .split() = um vetor/LINHA q lista valores em uma unica variavel
#EX: 
linha = input() .split() ou .split(" ")
    n1 = int(linha[0])
    n2 = int(linha[1])
    n3 = float(linha[2])
linha = n1 n2 n3
#ou
X1, Y1 = map(float ou int, input().split()) <--- MUITO mais simples

max = funcao q acha o maior valor de uma lista
abs = numero absoluto (ignora o sinal)

#interpolacao utiliza % para inserir valores em uma string
#ex:
# print("%i:%i:%i"%(hr,minu,seg))
# %s string
# %d ou i = inteiro 
# %o octal
# %x hexadecimal
# %f real
# %e realexponencial
# %e real exponencial# %% sinal de percentagem

#\n = quebra de linha

#while = condiçao enquanto
#ex
 N = 1
while N <= 10: (quando for maior igual a 10 vai parar o loop)
    if N % 2 == 0:
        print(f'{N} Eh par')
   else:
        print(f'{N} Eh impar')
    
    N += 1


#for = condicao para:
#               inicio | fim | incremento  (mais compacto q while, usar oq preferir)
for N in range(  1,      10,       1):
    if N % 2 == 0:
        print(f'{N} Eh par')
    else:
        print(f'{N} Eh impar')
        

#elif -- deixar codigo mais compacto
#ao inves de escrever:
if:
    blablabla
else:
    if:
        blablabla....
#escreve:
if:
  blabalbal...
elif:
   blablabla...

#sort
#organiza variaves de menor a maior
idades = [5 30 25 7 9 22 67 89 34]
idades.sort()
print(idades.sort())
5, 7, 9, 22, 25, 30, 34, 67, 89
0  1  2  ......................





#!!!!MANIPULACAO DE STRING!!!!

#list
list(frase) vai separar cada termo da string em seu proprio bloco
frase = 'ovo'
print list(frase)
['o','v','o']

#append
adiciona termo na string
fruta = [banana, maca, morango]
fruta.append(uva)
fruta = [banana, maca, morango, uva]
podemos manipular ONDE colocar o append tbm

#slice!
print(nomelista::0)

#len
len(frase) -------> mostra o tamanho da string (len = length)

#count
frase.count('letra') > conta quantas vezes uma variavel repete
frase.count('letra',0,14)> conta quantas vezes repete em um espaco determinado

#find
frase.find('x') mostras onde o termo comecou na string, quantas vezes tbm

#replace
frase = 'eu amo banana'
print(frase.replace('banana','canela'))
print >> 'eu amo canela'

#UPPER
frase.upper()-----vai deixar tudo em maiusculo
frase.lower()-----vai deixar tudo em minusculo


