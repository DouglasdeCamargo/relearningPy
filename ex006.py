#crie um algorítimo que leia um número e mostre o seu dobro, triplo e raíz quadrada

n1=float(input("insira o número: "))

dobro=2*n1
triplo=3*n1
raizquad=n1**(1/2)

print("O dobro de {} é: {} \nO triplo de {} é: {} \nA raiz quadrada de {} é: {}".format(n1,dobro,n1,triplo,n1,raizquad))