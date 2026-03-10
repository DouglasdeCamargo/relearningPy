#operadores aritiméticos: +(adição),-(subtração),*(multiplicação),/(divisão),**(potência),//(divisão inteira),%(resto)
5+2==7
5-2==3
5*2==10
5/2==2.5
5**2==25
5//2==2
5%2==0.5
#ordem de precedencia:(),**,* / // %, + -
#no python o tamanho máximo de um ponto flutuante, é o tamanho da memória
#serve para strings:
print("="*20)
 
#alinhamento de textos: <(alinhar à esquerda), >(alinhar à direita), ^(centralizar)
nome=str(input("qual seu nome?"))
print("Prazer em te conhecer {:=^20}!".format(nome))
#testando os operadores: 
n1=float(input("insira o primeiro valor:"))
n2=float(input("insira o segundo valor:"))
soma=n1+n2
sub=n1-n2
prod=n1*n2
div=n1/n2
divint=n1//n2
restodiv=n1%n2
exp=n1**n2
#utilidades no print:posso usar \n para fazer tudo em um único print, end=" ", para não quebrar linhaas de um print para o outro 
print("A soma de n1 e n2 é: {} \n A subitração de n1 e n2 é: {} \n O  produto de n1 e n2 é: {} \n A divisão de n1 por n2 é: {} \n A parte intera da divisão de n1 por n2 é: {} \n O resto da divisão de n1 por n2 é: {} \n  n1 elevado à n2 é: {}".format(soma,sub,prod,div,divint,restodiv,exp))
