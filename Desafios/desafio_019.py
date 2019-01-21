#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
from random import choice

n1 = input('Insira o primeiro aluno: ')
n2 = input('Insira o segundo aluno: ')
n3 = input('Insira o terceiro aluno: ')
n4 = input('Insira o quarto aluno: ')
lista = [n1, n2, n3, n3]
sorteio = choice(lista)

print('O aluno sorteado foi: {}!' .format(sorteio))