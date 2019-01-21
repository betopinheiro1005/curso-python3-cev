#Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a  
#sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro
#de tinta, pinta uma área de 2m^2

a = float(input('Qual é a altura da parede, em metros? '))
l = float(input('Qual é a largura da parede, em metros?'))
a = a*l
t = a/2

print('A área é {:2} m^2 e são necessários {} litros de tinta para pintar a parede.' .format(a, t))