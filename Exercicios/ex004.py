# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

n1 = input('Digite algo: ')
print(type(n1))
print('É numérico?', n1.isnumeric())
print('Está em maiúsculas?', n1.isupper())
print('Está em minúsculas?', n1.islower())
print('É alfabético?', n1.isalpha())
print('Só tem espaços?', n1.isspace())
print('É alfanumérico?', n1.isalnum())
