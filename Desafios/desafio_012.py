#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
#com 5% de desconto.

p = float(input('Qual o preço do produto? '))
des = float(p - ((5 * p) / 100))

print('O valor do produto com desconto de 5% é R${:2}' .format(des))