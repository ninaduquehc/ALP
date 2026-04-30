#Lista 3
#Marina Duque de Holanda Cavalcanti - DSM(1S26)
#1) Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
n=float(input('nota: '))
while n>10:
    print ('nota inválida! use números de 0 a 10')
    n=float(input('nota: '))
else:
    print ('nota válida')


#2) Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
n=input('nome: ')
s=input('senha: ')
while n==s:
    print ('erro! usuário e senha devem ser diferentes')
    n=input('nome: ')
    s=input('senha: ')
else:
    print ('nome e senha válidos!')

#3) Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
a=80000
b=200000
anos=0 
while a<b:
    a=a+a*0.03
    b=b+b*0.015
    anos=anos+1
print ('anos:',anos)

#4) A sequência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores. Faça um algoritmo que leia um número inteiro e calcule o seu número de Fibonacci. F₁ = 1, F₂ = 1, F₃ = 2, etc.
n=int(input("número: "))
if n<=0:
    print("o número deve ser inteiro e positivo.")
elif n==1 or n==2:
    print("fibonacci: 1")
else:
    a=1
    b=1
    k=1
    while k<=n-2:
        a,b=b,a+b
        k=k+1
    print("fibonacci: ",b)


#5) Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.
a=int(input('valor1: '))
b=int(input('valor2: '))
while a%b!=0:
    a,b=b,a%b
print("mdc:",b)




