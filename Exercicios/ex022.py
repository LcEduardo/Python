# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

numero = int(input('Digite um numero de 0 a 9999: '))

def extrair_digitos (number):

    unidade = number % 10
    dezena = (number // 10) % 10 
    centena = (numero // 100) % 10
    milhar = (numero // 1000) % 10

    return unidade, dezena, centena, milhar

unidade, dezena, centena, milhar = extrair_digitos(numero)
print(f'unidade: {unidade} \ndezena: {dezena} \ncentena: {centena} \nmilhar: {milhar}')