#fazer um palindromo
nome = input()
nome = list(nome)
novonome = []
for i in range(len(nome)):
    if nome[i] != (' '):
        novonome.append(nome[i])

        
tnome = len(list(novonome))
nomer = novonome[::-1]
print(novonome)
print(nomer)
 
ehpalindromo = True
for i in range(len(novonome)):
    if ((novonome[i]) != (nomer[i])):
        ehpalindromo = False
print(ehpalindromo)