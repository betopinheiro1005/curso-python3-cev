#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
#retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import pow 
from math import sqrt

co = float(input('Insira o cateto oposto do triângulo retângulo: '))
ca = float(input('Insira o cateto adjacente do triângulo retângulo: '))
h = (pow(co,2))+(pow(ca,2))
raiz = sqrt(h)

print('O comprimento da hipotenusa do triângulo é {:.2f}.' .format(raiz))