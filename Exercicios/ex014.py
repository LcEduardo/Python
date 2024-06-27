# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

graus = float(input('Digite a temperatura em ºC: '))
fahrenheit = (graus * 9/5) + 32
print(f'A temperatura em fahrenheit: {fahrenheit}ºF')