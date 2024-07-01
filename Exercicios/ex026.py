# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu nome: ')
segmento = nome.split()
first_name = segmento[0]
last_name = segmento[-1]
print(f'{first_name}\n{last_name}')
