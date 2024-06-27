# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angle = float(input('Digite um ângulo: '))

rad = radians(angle)

seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)

print(f'O ângulo em radianos é {rad:.4f}.')
print(f'O seno é {seno:.4f}.')
print(f'O cosseno é {cosseno:.4f}.')
print(f'A tangente é {tangente:.4f}.')