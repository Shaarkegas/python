lista = input().split(" ")
a = int(lista[0])
b = int(lista[1])
c = int(lista[2])
maiorAB = (a+b+abs(a-b))//2
maiorC = (maiorAB+c+abs(maiorAB-c))//2
print(maiorC, "eh o maior")

#outra alternativa

lista = input() .split(" ")
a = int(lista[0])
b = int(lista[1])
c = int(lista[2])
maiorAB = (a+b+abs(a-b))//2
if maiorAB > c :
    print(maiorAB, "eh o maior")
else:
    print(c, "eh o maior")

#outra OOOUTRA alternativa

a, b, c = map(int, input().split())
maiorAB = (a+b+abs(a-b))//2
if (maiorAB > c) :
    print(maiorAB, "eh o maior")
else:
    print(c, "eh o maior")