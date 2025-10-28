#Faça um programa que leia três números e mostre o maior deles
#Desenvolvido por: Debora

numero1=float(input("Digite o número 1: "))
numero2=float(input("Digite o número 2: "))
numero3=float(input("Digite o número 3: "))
maior=numero1
if numero2>maior:
    maior=numero2
if numero3>maior:
    maior=numero3
print(maior,"é o maior!")