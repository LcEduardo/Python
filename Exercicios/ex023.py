# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santos".

name_cidade = input('Escreva o nome da cidade: ')
primeiro_nome = name_cidade.split()
find = 'Santos' in primeiro_nome[0]

if find == True:
    print('A palavra Santos foi encontrada')
else: 
    print('A palavra Santos não foi encontrada')