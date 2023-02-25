"""nome = str(input('Qual é seu nome?'))
if nome == 'Bruno':
    print('Belo nome voce tem !')
else:
    print('Que nome feio {}'.format(nome))

print('Tenha um otimo dia')
TESTE     """

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

me= (n1+n2)/2

print('...........................................')
print('Sua media foi {:.1f}'.format(me))
print('...........................................')

if me >= 6:
    print('Parabens voce foi aprovado!')
else:
    print('Voce nao foi aprovado')

