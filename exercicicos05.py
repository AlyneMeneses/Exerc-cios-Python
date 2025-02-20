### WHILE ###
# n = 1
# while n != 0:
#     n = int(input('digite um valor:'))
# print('fim!')
import random

#--------------------------------------------------------------

sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo [M/F]:')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')

#---------------------------------------------------------------------------------

from random import randint
computador = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em um numer entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite:'))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[34mMais...Tente mais uma vez.\033[m')
        elif jogador > computador:
            print('\033[31mMenos... Tente mais uma vez.\033[m')
print(f'\033[32:1m--> Você acertou com {palpite} palpites.')


# ---------------------------------------------------------------------------

n1 = int(input('digite um valor:'))
n2 = int(input('dig ite um valor:'))
opcao = 0

while opcao != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMÉROS
    [5] SAIR DO PROGRAMA''')

    opcao = int(input('Qual sua opção:'))
    if opcao == 1:
        soma = n1 + n2
        print(f'\033[34mA soma de {n1} + {n2} é {soma}.\033[m')
    elif opcao == 2:
        mult = n1 * n2
        print(f'\033[34mA multiplicação de {n1} x {n2} é {mult}.\033[m')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f'\033[34mO maior é {maior}\033[m')
        if n1 < n2:
            maior = n2
            print(f'\033[34mO maior é {maior} \033[m')
    elif opcao == 4:
        print('Digite novos numéros:')
        n1 = int(input(f'primeiro numero:'))
        n2 = int(input(f'segundo numéro:'))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida!')
print('FIM DO PROGRAMA.')


# ------------------------------------------------------------------------------------------------

from math import factorial
n = int(input('digite um numéro:'))
f = factorial(n)
print(f'O factorial de {n} é {f}.')

OUTRA FORMA USANDO O WHILE:#

n = int(input('Digite uma numero para calcular seu Fatorial:'))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}',end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')

#---------------------------------------------------------------------------

num = cont = soma = 0
num = int(input('digite um numero [999 para parar]:'))
while num != 999:
    soma += num
    cont += 1
    num = int(input('digite um numero [999 para parar]:'))
print(f'Voce digitou {cont} numeros e a soma entre eles foi {soma}')

#------------------------------------------------------------------------------------
LEIA VARIOS NUMEROS, MOSTRE A MÉDIA ENTRE ELES E QUAL MAIOR E MENOR E SE QUER CONTINUAR.

resposta = 'S'
soma = quant = media = maior = menor = 0
while resposta in 'Ss':
    num = int(input('Digite um numéro:'))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print(f'Voce digitou {quant} numeros e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')


#-----------------------------------------------------------------------------

cont = soma = 0
while True:
    num = int(input('Digite um valor [999 para parar]:'))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')


#--------------------------------------------------------------------------
# TABUADAS

while True:
    n = int(input('Quer ver a tabuada de qual  valor?'))
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')




#------------------------------------------------------------------------------
#  IMPAR OU PAR (GUANABARA)

v = 0
while True:
    jogador = int(input('Diga um valor:'))
    computador = random.randint(1,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Impar ou Par? [P/I]')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total} ')
    print(f'--> Deu Par' if total % 2 == 0 else '--> Deu Impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU!')
        else:
            print('Voce PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU!')
            break
        print('Vamos jogar novamente...')

#-------------------------------------------------------------------------------------------------------

import random
print('=== JOGO DE PAR OU ÍMPAR ===')
while True:
    #entrada do jogaodor
    jogador_valor = int(input('\nDigite um valor:'))
    jogador_escolha = input('Par ou Ímpar [P/Í]:').strip().upper()[0]
    #geraçao do numero do computador
    computador_valor = random.randint(0,10)
    #soma dos valores
    soma = jogador_valor + computador_valor
    resultado = 'PAR' if soma % 2 == 0 else 'Ímpar'
    #exibir os valores escolhidos
    print(f'\nVocê jogou {jogador_valor} e o computador jogou {computador_valor}. Total: {soma} ({resultado})')
    #verifique quem ganhou
    if (jogador_escolha == 'P' and resultado == 'PAR') or (jogador_escolha == 'I' and resultado == 'ÍMPAR'):
        print('Você venceu!')
    else:
        print('Você perdeu!')
        break

    #ainda quer continuar?
    continuar = input('\nQuer jogar novamente? [S/N]:').strip().upper()[0]
    if continuar != 'S':
        print('Obrigado por jogar!')
        break

#----------------------------------------------------------------------------------

print('=== CADASTRO DE PESSOAS ===')
#VARIAVEIS PARA ARMAZENAR OS CONTADORES
mais_de_18 = 0
homens = 0
mulheres_menos_20 = 0

while True:
    idade = int(input('\nIdade:'))
    #entrada de sexo com validão
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F]').strip().upper()[0]
    #Processamento dos dados
    if idade > 18:
        mais_de_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

    #pergunte se o usuario quer continuar
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]').strip().upper()
    if continuar == 'N':
        break
#resultados finais
print('\n=== RESULTADOS ===')
print(f'A) Quantas pessoas tem mais de 18 anos: {mais_de_18}')
print(f'B) Quantos homens foram cadastrados: {homens}')
print(f'C) Quantas mulheres tem menos de 20 anos: {mulheres_menos_20}')

#-------------------------------------------------------------------------------

print('=== CADASTTRO DE PRODUTOS ===')

total = totmil = menor = cont = barato = 0
while True:
    produto = str(input('\nNome do Produto:'))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco

    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = input('\nQuer continuar? [S/N]').strip().upper()[0]
    if resp == 'N':
        break
print('\n=== RESULTADOS ===')
print(f'A) Total gasto na compra: R${total:.2f}')
print(f'B) Quantos produtos custam mais de R$1000: {totmil}')
print(f'C) Produto mais barato: {barato} que custa R$ {menor:.2f}')

#--------------------------------------------------------------------------------

print('=' * 30)
print('{:^30}'.format('BANCO DA ALYNE'))
print('=' * 30)

valor = int(input('Qual valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += ced
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('VOLTE SEMPRE!')

#---------------------------------------------------------------------------------


lanche = ('hamb', 'suco', 'pizza', 'pudim', 'arroz')

for comida in lanche:
    print(f'eu vou comer {comida}')

for pos, comida in enumerate(lanche): #MOSTRA A POSICAO NUMEREDA
    print(f'eu vou comer {comida} na posicao {pos}')

print(sorted(lanche)) #COLOCA O QUE ESTA DENTRO DA VARIAVEL LANCHE EM ORDEM ALFABETICA.

a = (1,2,3,4)
b = (3,3,7,1)
c = b + a
print(c.count(3)) # '.count' esta me informando quanto vezes aparece tal coisa.
print(c)
print(c.index(2)) # MOSTRA EM Q EXATA POSICAO ESTA ESTE ITEM

-----------------------------------------------------------------------------------

cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove','dez', 'onze', 'doze',
        'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito','dezenove','vinte')
continuar = 0
mais = 0
while True:
    numero = int(input('Digite um numero de 0 e 20:'))
    if 0 <= numero <= 20:
        break
    print(f'Voce digitou o numero {cont[numero]}')

    continuar = ' '
while True:
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if continuar in 'SN':
        break
    else:
        print('responsta invalida. digite novamente.')

print(f'Voce digitou o numero {cont[numero]}')


cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
        'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    # Solicita ao usuário um número entre 0 e 20
    while True:
        try:
            numero = int(input('Digite um número entre 0 e 20: '))
            if 0 <= numero <= 20:
                break
            else:
                print('Número fora do intervalo. Tente novamente.')
        except ValueError:
            print('Entrada inválida. Por favor, digite um número válido.')

    # Exibe o número por extenso
    print(f'Você digitou o número {cont[numero]}.')

    # Pergunta ao usuário se deseja continuar
    while True:
        continuar = input('Quer continuar? [S/N]: ').strip().upper()
        if continuar in ('S', 'N'):
            break
        else:
            print('Resposta inválida. Digite "S" para continuar ou "N" para encerrar.')

    # Encerra o loop principal se a resposta for "N"
    if continuar == 'N':
        print('Programa encerrado. Obrigado por utilizar!')
        break

-----------------------------------------

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
         'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo',
         'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminesce', 'Sport Recife',
         'EC Vitoria', 'Coritiba' , 'Avaí', 'Ponte Preta')

print('-' * 80)
print(f'Lista de times: {times}')
print('-' * 80)
print(f'-> Os 5 primeiros são {times[:5]}')
print('-' * 80)
print(f'-> Os 4 ultimos são {times[-4:]}')
print('-' * 80)
print(f'-> Times em ordem alfabetica{sorted(times)}')
print('-' * 80)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}° posição')
print('-' * 80)

---------------------------------------------------------------------------------------------------

from random import randint
numeros = tuple(randint(1,100)
for _ in range(5))

print(f'Numeros gerados{numeros}')
print(f'O maior numero é: {max(numeros)}')
print(f'O menor numero é: {min(numeros)}')

---------------------------------------------------------------------------

valores = (int(input('Digite um numero:')),
int(input('Digite um numero:')),
int(input('Digite um numero:')),
int(input('Digite um numero:')))

nove = valores.count(9)
print(f'O valor 9 apareceu {nove} vezes.')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}° posição.')
else:
    print('O valor 3 não apareceu.')
print('Os valores pares digitados foram ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')

----------------------------------------------------------------------------------

produtos = (
    'Arroz', 15.90,
    'Feijão', 9.75,
    'Macarrão', 5.50,
    'Óleo', 8.20,
    'Açucar', 4.80,
    'Leite', 7.60,
    'Café', 12.30,
    'Farinha', 6.30,
)
print('-' * 40)
print(f'{'LISTA DE PREÇOS':^40}')
print('-' * 40)

for i in range(0, len(produtos), 2):
    nome = produtos[i]
    preco = produtos[i + 1]
    print(f'{nome:<30} R${preco:7.2f}')
print('-' * 40)

---------------------------------------------------------------------

palavra = ('estudar', 'aprender', 'dormir', 'escovar', 'borboleta', 'castelo')
for p in palavra:
    print(f'\nNa palavra {p.upper()} tem --> ', end='')
    for vogais in p:
        if vogais.lower() in 'aeiou':
            print(vogais, end=' ')

----------------------------------------------------------------------------

valores = [3,5,2,9,7,5,1]
valores.sort()  # ELE COLOCA OS VALORES EM ORDEM CRESCENTE
valores.sort(reverse=True)  # COLOCA EM ORDEM DECRESCENTE
print(valores)

n = [3,5,7,7,1]
n.append(2)
n.insert(3,0)
n.pop(3)
print(n)

a = [1,2,3,4]
b = a[:] # IRA FAZER UMA COPIA DA VARIAVEL "a".
b[2] = 8
print(f'Lista A:{a}')
print(f'Lista B:{b}')

------------------------------------------------------------------------------------

lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}:')))
print(f'\nVoce digitou o valor {lista}')
print(f'O maior numero digitado foi {max(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end='')
print(f'\nO menor numero digitado foi {min(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...')

------------------------------------------------------------------------------

num = list()
while True:
    resp = int(input('Digite um valor:'))
    if resp not in num:
        num.append(resp)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor Duplicado! Não sera adicionado.')
    cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if cont == 'N':
        break
num.sort()
print(f'Voce adicionou os valores {num}')

------------------------------------------------------------------------------

lista = []
for c in range(0,5):
    n = int(input('Digite um valor:'))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'\nOs valores digitados ba ordem foram {lista}')

-------------------------------------------------------------------------

valores = []
while True:
    valores.append(int(input('Digite um numero:')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'\nVoce digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}.')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não se encontra na lista.')

---------------------------------------------------------------------------

valores = []
pares = list()
impares = list()
while True:
    valores.append(int(input('Digite um numero:')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista completa é {valores}.')
print(f'Os numeros pares são {pares}.')
print(f'Os numeros impares são {impares}.')

--------------------------------------------------------------------------------

temp = []
princ =[]
maior = menor = 0
while True:
    temp.append(str(input('Nome:')))
    temp.append(float(input('Peso:')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append((temp[:]))
    temp.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'\nAo todo, voce cadastrou {len(princ)} pessoas.')
print(f'\nO maior peso foi de {maior}Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}', end='')

---------------------------------------------------------------------------------

numero = [[],[]]
valor = 0
for c in range(1, 7):
    valor = int(input(f'Digite o {c}° valor:'))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)
numero[0].sort()
numero[1].sort()

print(f'Os valores pares digitados foram: {numero[0]}')
print(f'Os valores impares digitados foram {numero[1]}')

----------------------------------------------------------------------------------------

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}],[{c}]:'))
print('-' * 40)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

---------------------------------------------------------------------------------

print('=== MATRIZ 3x3 ===')
matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = coluna = maior = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor par [{l}], [{c}]:'))

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print()

print(f'\nA soma dos pares é igual a: {par}')
for l in range(0,3):
    coluna += matriz[l][2]
print(f'A soma dos valores da terciera coluna é: {coluna}')
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior}')

---------------------------------------------------------------------------------

import random

# Exibindo cabeçalho
print('-' * 30)
print('      JOGA NA MEGA SENA       ')
print('-' * 30)

# Solicita a quantidade de jogos a serem gerados
quant = int(input('Quantos jogos você quer que eu sorteie? '))

# Lista para armazenar os jogos
jogos = []

# Gerando os jogos
for _ in range(quant):
    jogo = []
    while len(jogo) < 6:
        num = random.randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    jogos.append(jogo)

# Exibindo os jogos sorteados
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, jogo in enumerate(jogos, start=1):
    print(f'Jogo {i}: {jogo}')
print('-=' * 5, ' BOA SORTE! ', '-=' * 5)

----------------------------------------------------------------------------------

ficha = list()
while True:
    nome = str(input('Nome:'))
    n1 = float(input('Nota 1:'))
    n2 = float(input('Nota 2:'))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 20)
print(f'{'N°':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-=' * 20)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 20)
    opc = int(input('Mostrar notas de qual aluno? [999 interromper]:'))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'--> Notas de {ficha[opc][0]} são de {ficha[opc][1]}')
print('\n<<< VOLTE SEMPRE >>>')

------------------------------------------------------------------------------

filme = {'titulo':'Star Wars',
         'ano':'1977',
         'diretor':'George Lucas'
}
print(filme.values()) # MOSTRA O VALOR (Star Wars, 1977, Geroge)
print(filme.keys())  # MOSTRA AS CHAVES (titulo, ano, diretor)
print(filme.items()) # MOSTRA TUDO

del filme['diretor'] # ISSO APAGA A CHAVE E O VALOR DESSA
filme['titulo'] = 'Panic' # ISSO SUBSTITUIU O TITULA QUE ESTAVA POR OUTRO
filme['tempo'] = 1.45 # ISSO ADICIONA UM VALOR
for k, v in filme.items():
    print(f'O {k} é {v}')


brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1) # ADICIONANDO OS ESTADOS EM UMA LISTA
brasil.append(estado2)
print(brasil[0]) # IRÁ MOSTRAR O VALOR DE 0 QUE SERIA RIO DE JANEIRO
print(brasil[1]['sigla']) # ESTA DEIXANDO EXPECIFICADO


estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa:'))
    estado['sigla'] = str(input('Sigla do Estado:'))
    brasil.append(estado.copy()) # ESTA É A FORMA QUE NA FUNÇÃO DIC.. DEIXA COPIAR O CONTEUDO.
for e in brasil: # PARA CADA ESTADO EM BRASIL, MOSTRE O ESTADO.
    print(e)

-------------------------------------------------------------------------------------------

aluno = dict()
aluno['nome'] = str(input('Nome:'))
aluno['média'] = float(input(f'Média de {aluno["nome"]}:'))
if aluno['média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')

------------------------------------------------------------------------------------------

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6),}
ranking = list()
print('=== VALORES SORTEADOS ===')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 20)
print('---> RANKING DOS JOGADORES <---')
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    print('-' * 25)
    sleep(1)

-----------------------------------------------------------------------------

from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome:'))
nasc = int(input('Ano de Nascimento:'))
idade = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem):'))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação:'))
    dados['aposentadoria'] = ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f' - `{k} tem o valor de {v}')

---------------------------------------------------------------------------

# Dicionário para armazenar os dados do jogador
jogador = {}

# Lista para armazenar os gols por partida
gols_por_partida = []

# Coleta de dados
jogador['nome'] = input('Nome do jogador: ').strip()
while True:
    try:
        total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
        if total_partidas < 0:
            print('O número de partidas não pode ser negativo. Tente novamente.')
        else:
            break
    except ValueError:
        print('Por favor, insira um número válido.')

# Coleta de gols por partida
for partida in range(total_partidas):
    while True:
        try:
            gols = int(input(f'Quantos gols {jogador["nome"]} fez na partida {partida + 1}? '))
            if gols < 0:
                print('O número de gols não pode ser negativo. Tente novamente.')
            else:
                gols_por_partida.append(gols)
                break
        except ValueError:
            print('Por favor, insira um número válido.')

# Calcula o total de gols e armazena os dados no dicionário
jogador['gols'] = gols_por_partida
jogador['total'] = sum(gols_por_partida)

# Exibe os dados do jogador
print('-=' * 30)
print(f'{"DADOS DO JOGADOR":^60}')
print('-=' * 30)

for chave, valor in jogador.items():
    print(f'{chave.capitalize()}: {valor}')

print('-=' * 30)
print(f'{"DESEMPENHO POR PARTIDA":^60}')
print('-=' * 30)

# Exibe o desempenho por partida
for i, gols in enumerate(jogador['gols']):
    print(f'Na partida {i + 1}, {jogador["nome"]} fez {gols} gol(s).')

print('-=' * 30)
print(f'{jogador["nome"]} marcou um total de {jogador["total"]} gol(s) no campeonato.')

-----------------------------------------------------------------------------------------

pessoa = {}
galera = list()
soma = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome:'))
    while  True:
        pessoa['Sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
        if pessoa['Sexo'] in 'FM':
            break
        print('ERRO! Por favor, digite F ou M.')
    pessoa['Idade'] = int(input('Idade:'))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        continuar = str(input('Quer continuar: [S/N]')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Por favor, digite S ou N.')
    if continuar in 'N':
        break
media = soma / len(galera)
print('-='*30)
print(f'--> A) Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'--> B) A média de idade entre elas é {media} anos.  ')
print(f'--> C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p["Sexo"] in 'F':
        print(f'`{p["Nome"]}')
print()
print('Listas de pessoas que estão acima da média: ')
for p in galera:
    if p['Idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'`{k} = {v}; ', end='')
print('===> ENCERRANDO <===')

------------------------------------------------------------------------------













