# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Exercícios extras

# G. verbing
# Dada uma string, caso seu comprimento seja pelo menos 3,
# adiciona 'ing' no final
# Caso a string já termine em 'ing', acrescentará 'ly'.
# dica use s.endswith('ing')
def verbing(s):
    if len(s) < 3:
        return s
    elif s.endswith('ing'):
        return s + 'ly'
    else:
        return s + 'ing'


# H. not_bad
# Dada uma string, procura a primeira ocorrência de 'not' e 'bad'
# Se 'bad' aparece depois de 'not' troca 'not' ... 'bad' por 'good'
# Assim 'This dinner is not that bad!' retorna 'This dinner is good!'
# dica use s.find('not') e s.find('bad') para ver as posições
def not_bad(s):
  nop=s.find('not')
  ruim=s.find('bad')
  if nop!=-1 and ruim!=-1 and nop<ruim:
    return s[:nop]+'good'+s[ruim+3:]
  return s


# I. inicio_final
# Divida cada string em dois pedaços.
# Se a string tiver um número ímpar de caracteres
# o primeiro pedaço terá um caracter a mais,
# Exemplo: 'abcde', divide-se em 'abc' e 'de'.
# Dadas 2 strings, a e b, retorna a string
# a_inicio + b_inicio + a_final + b_final
def inicio_final(a, b):
    meio_a = (len(a) + 1) // 2
    meio_b = (len(b) + 1) // 2
    a_inicio = a[:meio_a]
    a_final = a[meio_a:]
    b_inicio = b[:meio_b]
    b_final = b[meio_b:]
    return a_inicio + b_inicio + a_final + b_final


# J. zeros finais
# Verifique quantos zeros há no final de um número inteiro positivo
# Exemplo: 10010 tem 1 zero no fim e 908007000 possui três
# dica transforme para texto e inverta
# n = str(n)
# n = n[::-1]
def zf(n):
    soma = 0
    n = str(n)
    n = n[::-1]
    for a in n:
        if a == '0':
            soma = soma + 1
        else:
            break
    return soma


# K. conta 2
# Verifique quantas vezes o dígito 2 aparece entre 0 e n-1
# Exemplo: para n = 20 o dígito 2 aparece duas vezes entre 0 e 19
def conta2(n):
    soma = 0
    for a in range(n):
        for digito in str(a):
          if digito=='2':
            soma=soma+1
    return soma


# L. inicio em potencia de 2
# Dado um número inteiro positivo n retorne a primeira potência de 2
# que tenha o início igual a n
# Exemplo: para n = 65 retornará 16 pois 2**16 = 65536
# dica transforme para texto a potencia de 2
# e use .startswith(str(n))
def inip2(n):
  for a in range(10000):
    potencia=str(2**a)
    if potencia.startswith(str(n)):
      return a


def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'

    print('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))


def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('inicio_final')
    test(inicio_final('abcd', 'xy'), 'abxcdy')
    test(inicio_final('abcde', 'xyz'), 'abcxydez')
    test(inicio_final('Kitten', 'Donut'), 'KitDontenut')

    print()
    print('zeros finais')
    test(zf(10100100010000), 4)
    test(zf(90000000000000000010), 1)

    print()
    print('conta 2')
    test(conta2(20), 2)
    test(conta2(999), 300)
    test(conta2(555), 216)

    print()
    print('inicio p2')
    test(inip2(7), 46)
    test(inip2(133), 316)
    test(inip2(1024), 10)


if __name__ == '__main__':
    main()



