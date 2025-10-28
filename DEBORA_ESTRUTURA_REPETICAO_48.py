#Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
#Desenvolvido por: Debora 

#Exemplo:
#12376489
#=> 98467321

#int:números inteiros
numero=int(input("Sequência de Nº inteiros positivos: "))
#str:transforma o número em texto e "[::-1]"inverter os numeros
invertido=str(numero)[::-1]
print("invertido:",invertido)
