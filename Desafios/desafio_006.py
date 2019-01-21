#Crie um algoritmo que leia um número e mostre o seu dobro, seu triplo e a raiz quadrada.
n = int(input('Insira um número: '))
d = n * 2
t = n * 3
r = n ** 2

print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {}.' .format(n, d, t, r))