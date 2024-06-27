# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que a cada litro de tinta, pinta uma área de 2m2

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
conversao = round(area / 2, 2)
print(f'A quantidade de tinta para pintar a parede com área de {area}m2 é {conversao} litros de tinta.')
