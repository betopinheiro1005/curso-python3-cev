#Desenvolva um programa que leia as duas notas de um aluno,
#calcule e mostre a sua média
nome = input('Nome do aluno: ')
p1 = float(input('Nota da P1: '))
p2 = float(input('Nota da P2: '))
s = p1 + p2
m = s / 2

print('A média do aluno(a) {} é {}.' .format(nome, m))