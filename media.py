#media com 3 termos
n1, n2, n3, n4 = map(float, input().split())
media = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10

if media >= 7.0 :
    print('Media: %.1f' % media)
    print('Aluno aprovado.')

elif (media>=5.0) and (media<=6.9) :
    print('Media: %.1f' % media)
    print('Aluno em exame.')
    ne = float(input())
    print('Nota do exame: %.1f' % ne)
    mediaf = (ne+media)/2
    
    if mediaf >= 5.0 :
        print('Aluno aprovado.')
        print('Media final: %.1f' % mediaf)
    else:
        print('Aluno reprovado.')
        print('Media final: %.1f' % mediaf)
else:
    print('Media: %.1f' % media)
    print('Aluno reprovado.')