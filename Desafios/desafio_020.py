#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import sample

n1 = input('Insira o 1 aluno: ')
n2 = input('Insira o 2 aluno: ')
n3 = input('Insira o 3 aluno: ')
n4 = input('Insira o 4 aluno: ')
lista = sample([1, 2, 3, 4], k=4)

print('Sorteio: {}' .format(lista))
