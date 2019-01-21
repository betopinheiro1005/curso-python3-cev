#Faça um algoritmo que leia o salário de um funcionário e mostre seu
#novo salário, com 15% de aumento.

s = float(input('Qual é o seu salário? '))
a = float(((s*15)/100)+ s)

print('O seu salário com aumento de 15% ficará sendo R${:2}' .format(a))