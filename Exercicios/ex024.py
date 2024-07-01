# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome_pessoa = input('Digite seu nome: ')
find = "Silva" in nome_pessoa

if find == True:
    print(f'O nome {nome_pessoa} tem "Silva"')
else:
    print(f'O nome {nome_pessoa} não tem "Silva"')