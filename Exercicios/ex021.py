# Crie um programa que leia o nome completo de uma pessoa e mostre: com letra maiúscula, letra minúscula, quantas letras ao todo (sem espaços) e quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ')
print(f'Nome com letras maiúsuculas: {nome.upper()}')
print(f'Nome com letras minúsuculas: {nome.lower()}')
print(f'Total de letras sem espaço: {len(nome.replace(' ', ''))}')
primeiro_nome = nome.split()
print(f'Quantas letras tem o primeiro nome: {len(primeiro_nome[0])}')