# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar

money = float(input('Quanto de dinheiro você tem na carteira: '))
conversao = round(money / 5.51, 2)
print(f'Com esse dinheiro eu posso comprar ${conversao:.2f} dolar americano.')