frase = 'Vamos jogar bola hoje'

print(f'{len(frase)}')
print(f'{frase.count('o')}')
print(f'{frase.count('o',0,16)}')
print(f'{frase.find('bola')}') # mostra o índice que começa
print(f'{frase.find('game')}') # -1 quer dizer que não foi encontrado.
print(f'{'vamos' in frase}')
print(f'{'Vamos' in frase}')