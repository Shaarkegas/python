x, y = map(float,input().split())
if (x>0) and (y>0):
    print('Q1')

elif (x<0) and (y>=1):
    print('Q2')

elif (x<0) and (y<0):
    print('Q3')

elif (x>=1) and (y<0):
    print('Q4')

elif (x==0) and (y==0):
    print('Origem')

elif (y==0):
    print('Eixo X')

else:
    print('Eixo Y')