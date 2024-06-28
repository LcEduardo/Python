# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.

from random import shuffle

participantes = []

num_participantes = int(input('Número de participantes do grupo: '))
for i in range(num_participantes):
    nome_participante = input(f'Digite o nome do participante {i + 1}: ')
    participantes.append(nome_participante)

shuffle(participantes)
print(f'A nova ordem: {participantes}')

