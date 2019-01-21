#Faça um programa que leia um ângulo qualquer e mostre
#na tela o valor do seno, cosseno e tangente desse ângulo.
from math import cos, tan, sin

a = int(input('Insira um ângulo: '))

print('O ângulo {} possui seno {:2f}, cosseno {:2f} e tangente {:2f}.' .format(a, sin(a), cos(a), tan(a)))