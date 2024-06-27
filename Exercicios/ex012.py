# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Digite o preço do produto: '))
desconto = produto * 0.05
preco = produto - desconto
print(f'O preço do produto com 5% de desconto é: R${preco}')