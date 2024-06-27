# Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

participantes = []

num_participantes = int(input('Digite o número de participantes: '))
for i in range(num_participantes):
    nome_participante = input(f'Digite o nome do participante {i + 1}: ')
    participantes.append(nome_participante)

print(f'O nome do vencedor é {choice(participantes)}')