"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
"""

print('-'*20)
print('SEQUÊNCIA FIBONACCI')
print('-'*20)

n= int(input('Entre com um número Inteiro: '))

t1=0
t2=1

print(f'{t1} --> {t2}', end='')
contador=3 #pois ja tem o primeiro e o segundo termo (t1 e t2)

fibonacci= [t1, t2] #armazenar

while contador <=n:
    t3= t1 + t2
    print(f' --> {t3}', end='')
    fibonacci.append(t3) #armazenar t3
    t1= t2
    t2=t3
    contador += 1

print('--> FIM')

#verificando se o número que o usuário digitou inicialmente pertence a sequência

if n in fibonacci:
    print(f'O número {n} pertence a sequência Fibonacci')

else:
    print(f'O número {n} NÃO pertence a sequência Fibonacci')

