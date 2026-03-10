#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor 

n1=int(input("insira o número: "))
sus=int(n1+1)
ant=int(n1-1)

print("o antecessor de {} é {} e o o sussesor é {}".format(n1,ant,sus))
