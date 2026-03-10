#desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média
nome=str(input("Nome do aluno: "))
n1=float(input("Nota 1: "))
n2=float(input("Nota 2: "))
n3=float(input("Nota 3: "))
m=(n1+n2+n3)/3

print("a média aritimética do aluno {} é: {}".format(nome,m))