from math import radians, sin, cos, tan
angulo = float(input('digite o angulo que voçê deseja: '))
seno = sin(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cos = cos(radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}'. format(angulo, cos))
tan = tan(radians(angulo))
print('O angulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tan))