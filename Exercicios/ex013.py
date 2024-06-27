# Faça um algoritimo que leia o salário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite seu sálario aqui: '))
aumento = salario * 0.15
print(f'Seu salário receberá um aumento de R${aumento} \nSeu salário final é: R${aumento + salario}.')