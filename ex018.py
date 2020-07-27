# exercicio 18
# leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

from math import radians, sin, cos, tan
ângulo = float(input('Digite o angulo que deseja:'))
seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem a TAMGEMTE de {:.2f}'.format(ângulo, tangente))