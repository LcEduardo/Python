# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc

real_number = float(input('Digite qualquer número real: '))
int_number = trunc(real_number)
print(f'A parte inteira desse número é: {int_number}')