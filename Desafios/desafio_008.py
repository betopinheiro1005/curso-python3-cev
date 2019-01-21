#Escreva um programa que leia um valor em metros e o 
#exiba convertido em centimetros e milimetros.

n = int(input('Insira um valor em metros: '))
c = n * 100
m = n * 1000

print('O valor {} metros é o mesmo que {} centímetros e {} milímetros.' .format(n, c, m))