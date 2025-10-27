#Faça um programa que verifique se uma letra digitada é vogal ou consoante.
#desenvolvido por : Debora

letra=input("Escreva uma letra:")
#if:se in:verifica se algo está dentro de outra coisa
if letra in "aeiou":
    print("Essa letra é uma vogal.")
#senao
else:
    print("Essa letra é uma consoante.")