#Crie um programa que leia um número Real qualquer pelo teclado e mostre
#na tela a sua porção inteira.
from math import trunc

n = float(input('Digite um número Real: '))
print('A parte inteira desse número é {}' .format(trunc(n)))