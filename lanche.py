cod, quant = map(int, input().split())
if cod == 1:
    t = quant*4.00
    print('Total: R$ %.2f' % t )
elif cod == 2:
    t = quant*4.50
    print('Total: R$ %.2f' % t )
elif cod == 3:
    t = quant*5.00
    print('Total: R$ %.2f' % t )
elif cod == 4:
    t = quant*2.00
    print('Total: R$ %.2f' % t )
elif cod == 5:
    t = quant*1.50
    print('Total: R$ %.2f' % t )