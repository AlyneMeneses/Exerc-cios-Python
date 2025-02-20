nome = str(input('qual seu nome?'))
if nome == 'Alyne': # AQUI VOCÊ PODE COLOCAR O SEU
    print('Que nome lindo!!!')
print(f'Bom dia',nome)


# OUTROS JEITOS DE RESPONDER

nome = str(input('qual seu nome?')).strip()
if nome == 'Alyne':
    print('Que nome lindo!!!')
else:
    print('seu nome é simplis :/')
print(f'Bom dia',nome)


# NESTE CODIGO ELE TE DA A MEDIA DAS SUAS NOTAS E FALA SE VOCE PASSOU OU NAO.

nota1 = float(input('digite a primeira nota:'))
nota2 = float(input('digite a segunda nota:'))
media = (nota1 + nota2) /2
print(f'A sua média foi', media)
if media >= 6.0:
    print('APROVADOOOOOOO, parabéns!')
else:
    print('Ih! não passou. Vá estudar!!!!!!')

#---------------------------------------------------------------#

#DESAFIO: PENSE EM UM NÚMERO DE 0 A 5

import random
from time import sleep
n_computador = random.randint(0,5)
print('Pensei em um numero entre 0 e 5. Consegue adivinhar qual é?')
n_usuario = int(input('Digite seu palpite:'))
print('PROCESSANDO...', )
sleep(3)
if n_usuario == n_computador:
    print('Acertou em cheio. Parabéns!! :). Eu realmente oensei no número', n_computador)
else:
    print('Que pena, você errou, eu pensei no número', n_computador)

#---------------------------------------------------------------------------------------------

# SE ULTRAPASSAR 80km/h GANHA MULTA.

velocidade = float(input('Digite a velocidade do carro em km/h:'))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado! Sua velocidade foi {velocidade:.1f}km/h\n'
          f'A multa é de R${multa:.2f}')
print('\033[33m Tenha um bom dia. Dirija com cuidado.\033[33m')

#-------------------------------------------------------------------------------------

# Programa para verificar se um número é par ou ímpar


numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é\033[33m par.\033[33m")
else:
    print(f"O número {numero} é\033[35m ímpar.\033[35m")


#-----------------------------------------------------------------------------------------

# PROGRAMA PARA CALCULAR O PREÇO DA VIAGEM

distancia = float(input('Qual a distância da sua viagem?'))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.40
print(f'O preço da sua passagem é de R${preco:.2f}')
print('\033[35m ------------------------------------ \033[35m')


#--------------------------------------------------------------------------------------------------

# JOGO DA ADIVINHAÇÃO: O OBJETIVO É ACERTAR EM QUAL NUMEERO A MAQUINA "PENSOU".
import random
maquina = random.randint(0,5)
print('-=-' *26)
print(' JOGO DA ADVINHAÇÃO / JOGO DA ADVINHAÇÃO / JOGO DA ADVINHAÇÃO')
print('-=-' *26)
print('Tende advinhar em qual número eu pensei de 1 a 5! ')
jogador = int(input('Digite:'))
if jogador == maquina:
    print(f'EITA!!! Mandou bem. Eu realmete pensei no {maquina}\n✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨')
else:
    print('Errou\n😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂')


#-------------------------------------------------------------------------------------------------------------------------------

# MOSTRA SE O ANO É BISSEXTO #

from datetime import date

ano = int(input('Que ano quer analizar?'))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} NÃO é bissexto')

#------------------------------------------------------------------------------

# MAIOR E MENOR VALORE #

a = int(input('Digite um numero:'))
b = int(input('Digite um numero:'))
c = int(input('Digite um numero:'))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c>b:
    maior = c
print(f'O menor valor é:{menor}')
print(f'O maior valor é:{maior}')

#--------------------------------------------------------------------------------

# MOSTRA QUEM IRA GANHAR UM AUMENTO NO SALÁRIO.

salario = float(input('Qual é o salario do funcionario?'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'Quem ganhava {salario:.2f}, vai passar a ganhar {novo:.2f}.')

#-------------------------------------------------------------------------------

# ANALISANDO TRIÂNGULO #

r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo1')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')

#-------------------------------------------------------------------------

# É ASSIM QUE COLOCA CORES EM PYTHON#

print('\033[4:30:43m ALYNE \033[4:30:43m')


# \033[0:33:40m (exemplo)
#
# - STYLE
#
# 0 (nada)
# 1 (Bolde)
# 4 (Underline)
# 7 (Negative)
#
# - TEXT
#
# 30 (branco)
# 31 (vermelho)
# 32 (verde)
# 33 (amarelo)
# 34 (azul)
# 35 (roxo)
# 36 (ciano)
# 37 (cinza)
#
# - BACK
#
# 40 (branco)
# 41 (vermelho)
# 42 (verde)
# 43 (amarelo)
# 44 (azul)
# 45 (roxo)
# 46 (ciano)
# 47 (cinza)

#------------------------------------------------------------------------------------

