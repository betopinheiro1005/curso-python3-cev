#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
#quantos Dólares ela pode comprar. Considerando: US$1.00 = R$3.27

d = float(input('Quanto dinheiro você tem na carteira? '))
v = d / 3.27

print('O valor que você tem corresponde a US${:2f}.' .format(v))