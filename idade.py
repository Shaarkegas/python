#converter x quantidade de dias para anos meses e dias
ndias = int(input())
anos = ndias//365
ndias = ndias%365
mes = ndias//30
dias = ndias%30
print(f'{anos} ano(s)')
print(f'{mes} mes(es)')
print(f'{dias} dia(s)')