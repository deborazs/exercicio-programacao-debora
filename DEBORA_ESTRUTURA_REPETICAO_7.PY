#Faça um programa que leia 5 números e informe o maior número.
#Desenvolvido por: Debora
numero1=float(input("Digite o 1º número:"))
numero2=float(input("Digite o 2º número:"))
numero3=float(input("Digite o 3º número:"))
numero4=float(input("Digite o 4º número:"))
numero5=float(input("Digite o 5º número:"))
maior=numero1
if numero2>maior:
    maior=numero2
if numero3>maior:
    maior=numero3
if numero4>maior:
    maior=numero4
if numero5>maior:
    maior=numero5

print(maior,"é o maior!")