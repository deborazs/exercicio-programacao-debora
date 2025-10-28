#Faça um programa que peça dois números e imprima o maior deles.
#Desenvolvido por: Debora

#float:números decimais
numero1=float(input("Digite primeiro número:"))
numero2=float(input("Digite o segundo número:"))

maior=numero1
if numero2>maior:
  maior=numero2

print(maior,"é o maior!")