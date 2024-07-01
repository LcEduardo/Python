# Faça um programa que leia uma frase pelo teclado e mostre: quatas vezes aparece a letra "a", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('Digite uma frase ai: ')
quant_a = frase.count("a")
first_a = frase.find("a")
last_a = frase.rfind("a")
print(f'O número de vezes que aparece a letra a é: {quant_a} \nEla aparece pela primeira vez no índice {first_a } \nEla aparece pela ultima vez no índice {last_a}')
