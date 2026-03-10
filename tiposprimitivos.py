#deve-se colocar o tipo de dado, antes do input, ou antes de declarar a variável
#são tipos primitivos: int, float, str, bool
#caso haja dúvida sobre o tipo da varável, posso usar a funcionalidade type()
#o comando isnumeric, isalpha me permite conferir se é possível converter de um tipo para outro

n1=int(input('insira o primeiro número:'))
n2=int(input('insira o segundo número: '))
s=n1+n2 
print('o valor da soma é: {}'.format(s))
print('a soma entre {} e {} vale: {}'.format(n1,n2,s))
print(type(s))