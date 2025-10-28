#Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
#F - Feminino
#M - Masculino
#Sexo Inválido.
#desenvolvido por : Debora

letra=input("Digite 'F' ou 'M':")
if letra=="F":
    print("Feminino.")
elif letra=="M":
    print("Masculino.")
else:
    print("Sexo Inválido!")