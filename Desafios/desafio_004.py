#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
#e todas as informações possíveis sobre ele.

a = str(input('Digite uma palavra: '))
print(a.islower())#verifica se todos os caracteres da string estão em caixa baixa

b = str(input('Digite um título: '))
print(b.istitle())#verifica so primeiro caractere da string está em caixa alta

c = str(input('Digite outra coisa: '))
print(c.islower())#verifica se a string está em caixa baixa

d = input('Digite algo: ')
print(d.isalnum())#verifica se a string é alfanumérica

e = str(input('Digite algo: '))
print(e.isalpha())#verifica a string contém apenas letras

f = input('Digite algo: ')
print(f.isdigit())#verifica se a string contém apenas números

g = str(input('Digite algo: '))
print(g.isspace())#verifica se a string contém apenas espaços

#https://wiki.python.org.br/ManipulandoStringsComPython