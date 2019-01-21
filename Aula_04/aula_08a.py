from math import sqrt
#from math import sqrt, floor
#from math import sqrt, ceil
#import math
num = int(input('Digite um número: '))
#raiz = math.sqrt(num)
raiz= sqrt(num)
#print('A raiz de {} é igual a {}.' .format(num, raiz))
#print('A raiz de {} é igual a {}.' .format(num, math.ceil(raiz)))#arredondado para cima
#print('A raiz de {} é igual a {}.' .format(num, math.floor(raiz)))#arredondado para baixo
print('A raiz de {} é igual a {:.2f}.' .format(num, raiz))

