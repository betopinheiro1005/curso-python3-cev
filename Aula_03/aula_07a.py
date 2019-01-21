#outra forma de replicar informações
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {}!' .format(nome)) # {:20} faz o nome aparecer dentro de 20 caracteres
# {:>20} faz o nome aparecer dentro de 20 caracteres alinhado a direita, o inverso a esquerda
# {:^20} faz o nome aparecer centralizado dentro de 20 caracteres(espaços)
# {:=^20} faz o nome aparecer centralizado dentro de 20 caracteres, sendo os restantes o = 

n1 = int(input('Insira um valor: '))
n2 = int(input('Insira outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
#print('A soma vale {}' .format(n1 + n2))
print('A soma é {}, o produto é {} e a divisão é {:.f}.' .format(s, m, d), end='')#3f -> 3 casas decimais flutuantes, end='' -> no final da linha, não irá quebrar linha para o próximo print
print('A divisão inteira é \n{} e a potência é {}.' .format(di, e))#\n -> quebra linha