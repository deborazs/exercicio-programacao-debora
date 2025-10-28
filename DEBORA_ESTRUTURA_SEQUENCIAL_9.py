#Faça um programa que peça a temperatura em graus Fahrenheit,transforme e mostre a temperatura em graus Celsius.
#Desenvolvido por: Debora 
#Formula
#C = 5 * ((F-32) / 9).

#float:números decimais
f=float(input("Qual a temperatura em graus Fahrenheit:"))
c = 5 * ((f-32) / 9) #formula
print(f,"em graus Celsius é:",c)
