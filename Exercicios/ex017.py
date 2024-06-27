# Faça um prorama que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

cat_op = float(input('Qual é a medida do cateto oposto: '))
cat_ad = float(input('Qual é a medida do cateto adjacente: '))

print(f'O calculo da hipotenusa do triangulo retangulo é {hypot(cat_ad, cat_op)}')

