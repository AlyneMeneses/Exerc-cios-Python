

#-----------------------------------------------------------------------------------------------------------------------
#CRIE UM ALGORITMO QUE LEIA UM NUMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA.

n = float(input('Digite um numero:'))
d = n * 2
t = n * 3
r = math.sqrt(n)
print(f'O dobro dele é:{d},\n O triplo é:{t} \ne a Raiz sera:{r}')

#-----------------------------------------------------------------------------------------------------------------------
#DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO,CALCULE E MOSTRE A SUA MÉDIA.

n1 = float(input('Digite a nota 1:'))
n2 = float(input('Digite a nota 2:'))
m = (n1 + n2) / 2
print(f'A media será:{m}')

#-----------------------------------------------------------------------------------------------------------------------

#FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO QUALQUER E MOSTRE NA TELA A SUA TABUADA.

n = int(input('Digite um numero inteiro:'))
print(f'Tabuada de {n} é:')
for i in range(1,11):
   print(f'{n} x {i}) = {n * i}')

#-------------------------------------------------------------------------------------------------------------------------------------------
#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR (CONSIDERE: US$1,00=R$3,37)

dinheiro = float(input(f'digite quanto dinheiro você tem:'))
cotaçao_dolar = 3.27
dolares = dinheiro / cotaçao_dolar
print(f'Com R${dinheiro: .2f}),voce pode comprar US${dolares:.2f}.')200

#=--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FAÇA UM PRGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA,PINTA UMA ÁREA DE 2m^2.

largura = float(input('largura:'))
altura = float(input('altura:'))
area = altura * largura
litros = 2
quantidade = area / litros
print(f'a area da parede é de {area: .2f} metros quadrados.')
print(f'voce precisara de {quantidade: .2f} litros de tinta para pintar')


#-----------------------------------------------------------------------------------------------------------------------

#PROGRAME UM ALGOTITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO.

preco = float(input('digite o preço do produto:'))
desconto = preco * 0.05
novo_preco = preco - desconto
print(f'preço original R${preco: .2f}.')
print(f'desconto R${novo_preco: .2f}')

#-----------------------------------------------------------------------------------------------------------------------

#FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO.

salario = float(input('salario:'))
aumento = salario * 0.15
novo_salario = salario + aumento
print(f'novo salario com 15% de aumento R${novo_salario: .2f}')

#-----------------------------------------------------------------------------------------------------------------------

#CONVERTA A TEMPERATURA DE °C PARA °F

c = float(input('Digite a temperatura em graus Celsius:'))
f = (c * 9/5) + 32
print(f'{c : .0f}°C equivalem a {f : .0f}°F')

#-----------------------------------------------------------------------------------------------------------------------

#CARRO ALUGADO

dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos km rodados?'))
pago = (dias * 60) + (km * 0.15)
print(f'O total a pagar é R${pago:.2f}')

#-----------------------------------------------------------------------------------------------------------------------

#UTILIZANDO MODULOS

import math
n = int(input('Digite um numero:'))
raiz = math.sqrt(n)
print(f'A raiz de {n} é {raiz}')

from math import sqrt
n = int(input('Digite um numero:'))
raiz = sqrt(n)
print(f'A raiz de {n} é {raiz :.2f}')

#-----------------------------------------------------------------------------------------------------------------------

#O METODO RANDOM DA CLASSE RANDOM GERA UM NUMERO ALEATORIO

import random
n = random.randint(1,10)
print(n)

#-----------------------------------------------------------------------------------------------------------------------

#PROGRAMA QUE LEIA UM NUMERO REAL QUALQUER PELP TECLADO E MOSTRE NA TELA A SUA PORÇAO INTEIRA.

n = float(input('digite um numero:'))
i = int(n)
print(f'o numero {n} tem sua parte interia {i}')

#-----------------------------------------------------------------------------------------------------------------------

#FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIANGULO RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA.

import math
cateto_oposto = float(input('digite o comprimento do cateto oposto:'))
cateto_adjacente = float(input('digite o comprimento do cateto adjacente:'))
hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)
print(f'o comprimento da hipotenusa é {hipotenusa:.2f}')

#----------------------------------------------------------------------------------------------------------------------------------------------------------

#FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ÂNGULO.

angulo = float(input('Digite um ângulo em grau:'))
angulo_radianos = math.radians(angulo)
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)
print(f'O ângulo de {angulo:.2f} tem:')
print(f'seno: {seno:.2f}')
print(f'cosseno: {cosseno: .2f}')
print(f'tangente: {tangente:.2f}')

#---------------------------------------------------------------------------------------------------------------------------------------------------

# SORTEAR UM ALUNO

a1 = input('digite o nome de um aluno:')
a2 = input('digite o nome de outro aluno:')
a3 = input('digite o nome de outro aluno:')
a4 = input('digite o nome de outro aluno:')

alunos = [a1,a2,a3,a4]
sorteado = random.choice(alunos) # sortear um dos 4 #
print(f'O aluno sorteado foi:{sorteado}')


#-----------------------------------------------------------------------------------------------------------------------------------

#AGORA QUE MOSTRE A ORDEM SORTEADA

a1 = input('digite o nome de um aluno:')
a2 = input('digite o nome de outro aluno:')
a3 = input('digite o nome de outro aluno:')
a4 = input('digite o nome de outro aluno:')

alunos = [a1,a2,a3,a4]

random.shuffle(alunos) #(embaralhar a ordem)
print('A ordem sorteado foi:')
for i, alunos in enumerate(alunos,1):
    print(f'{i}. {alunos}')

#----------------------------------------------------------------------------------------------------------------------------------

#FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O ÁUDIO DE UM ARQUIVO MP3.

import pygame

pygame.mixer.init() #(inicializa o mixer do pygame)
pygame.mixer.music.load('amor_fe.mp3') #(carregar arquivo)
pygame.mixer.music.play() #(reproduzir audio)
pygame.event.wait()

#--------------------------------------------------------------------------------------------------------------------------------