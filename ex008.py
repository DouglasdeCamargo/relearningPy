#escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros
m=float(input("insira a distância em metros: "))
cm=m*100
mm=m*1000

print("a distância em centímetros é: {}\n a distância em milímetros é: {}".format(cm,mm))