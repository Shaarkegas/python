id = int(input())
horas = int(input())
dinhora = float(input())
SALA = horas * dinhora
print("NUMBER =", id)
print("SALARY = U$ %.2f" % SALA)

# salario com bonus
NOME = input()
SALARIO = float(input())
VENDAS = float(input())
#BONUS DE 15% PARA CADA VENDA
TOTAL = (0.15*VENDAS + SALARIO)
print("TOTAL = R$ %.2f" % TOTAL)
