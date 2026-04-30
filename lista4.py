#Lista 4
#Marina Duque de Holanda Cavalcanti - DSM(1S26)

#1) Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.
import random
numeros=[]
for a in range(10):
    numeros.append(random.randint(1, 100))
maior=numeros[0]
menor=numeros[0]
for b in numeros:
    if b>maior:
        maior=b
    if b<menor:
        menor=b
print("lista: ", numeros)
print("maior número: ", maior)
print("menor número: ", menor)

#2) Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas.
import random
numeros=[]
for a in range(20):
    numeros.append(random.randint(1, 100))
impar=[]
par=[]
for b in numeros:
    if b%2==0:
        par.append(b)
    else:
        impar.append(b)
        
print("lista: ", numeros)
print("números pares: ", par)
print("números ímpares: ", impar)


#3) Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. Imprima os três vetores.

import random
vetor1=[]
vetor2=[]
for a in range(10):
    vetor1.append(random.randint(1, 100))
    vetor2.append(random.randint(1, 100))
    
vetor3=[]
for b in range(10):
    vetor3.append(vetor1[b])
    vetor3.append(vetor2[b])
    
print("vetor 1: ", vetor1)
print("vetor 2: ", vetor2)
print("vetor 3", vetor3)

#4) Seja o statement sobre diversidade: “The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.”. Gere uma lista de palavras deste texto com split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras “python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais e cuidado com maiúsculas e minúsculas.
texto='''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''
texto=texto.lower()
for a in ".,:":
    texto=texto.replace(a," ")
palavras=texto.split()
lista=[]
letras='python'
for b in palavras:
    if b[0] in letras or b[-1] in letras:
        lista.append(b)
print(f'resultado: {lista}')

#5) Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras “python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para minúsculas e de remover antes os caracteres especiais.
texto='''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''
texto=texto.lower()
for a in ".,:":
    texto=texto.replace(a," ")
palavras=texto.split()
lista=[]
letras='python'
for b in palavras:
    if len(b)>4:
        for c in letras:
            if c in b:  
                lista.append(b)
                break
print(f'quantidade: {len(lista)}')


v=random.sample(range(1,101),10)
v
[67, 91, 79, 5, 15, 60, 41, 18, 3, 11]



def pythonica(p):
    for letra in p:
        if letra in 'python':
            return True
    return False 
