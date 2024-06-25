# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Digite o valor em metros: '))
cm = round(metros * 100)
mm = round(metros * 1000)
print(f'cm: {cm} \nmm: {mm}')
