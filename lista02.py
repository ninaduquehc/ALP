#LISTA 2
#Marina Duque de Holanda Cavalcanti - DSM(1S26)

#1) Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))
if a>=b+c or b>=a+c or c>=a+b:
    print ('não é um triângulo')
else:
    if a==b or b==c or c==a:
        print ('é um triângulo isósceles')
    if a==b==c:
        print ('é um triângulo equilátero')
    else:
        print ('é um triângulo escaleno')

#curiosidade: 
l = sorted([a, b, c])
if l[2]**2 == l[0]**2 + l[1]**2:
    print ('é um triângulo retângulo') 

#2. Determine se um ano é bissexto. Verifique no Google como fazer isso…
a=int(input('ano: '))
if a%4==0 and (a%100!=0 or a%400==0):
  print('ano bissexto')
else:
  print('ano não bissexto')

#3. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.
p=float(input('peso de peixes: '))
if p<50:
    print (f'multa: ZERO')
if p>50:
    print (f'excesso:{p-50:.2f}')
    print (f'multa:{(p-50)*4:.2f}')

#4. Faça um Programa que leia três números e mostre o maior deles.
a=float(input('valor1: '))
b=float(input('valor2: '))
c=float(input('valor3: '))
if a>=b and a>=c:
    print (f'maior:{a}')
elif b>=c and b>=a:
    print (f'maior:{b}')
elif c>=a and c>b:
    print (f'maior:{c}')


#5. Faça um Programa que leia três números e mostre o maior e o menor deles.
a=float(input('valor1: '))
b=float(input('valor2: '))
c=float(input('valor3: '))
if a>=b and a>=c:
    print (f'maior:{a}')
elif b>=c and b>=a:
    print (f'maior:{b}')
else:
    print (f'maior:{c}')

if a<=b and a<=c:
    print(f'menor:{a}')
elif b<=c and b<=a:
    print(f'Menor:{b}')
else:
    print(f'Menor:{c}')

#6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido.
#Observe que: Salário Bruto - Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindica to ( 5%) : R$ 
#= Salário Liquido : R$
v=float(input('valor do salário por hora: '))
h=int(input('horas trabalhadas no mês: '))
b=v*h 
r=b*11/100
n=b*8/100
s=b*5/100
l=b-(r+n+s) 
print (f'salário bruto: R${b:.2f}')
print (f'IR(11%): R${r:.2f}')
print (f'INSS(8%): R${n:.2f}')
print (f'sindicato(5%): R$ {s:.2f}')
print (f'salário líquido: R${l:.2f}')

#7. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$80,00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas
t=float(input('tamanho em metros quadrados: '))
if t%54==0:
    l=m/54
else:
    l=int(t/54)+1
v=l*80
print(f'quantidade de latas: {l}')
print(f'preço total: R$ {v}')