# O QUE SÃO FUNÇÕES OU ROTINAS (def)

def soma(a, b):
    s = a + b
    print(f'A soma de {a} com {b} é igual a {s}')


soma(100, 23)
soma(12, 89)
soma(123, 999)

---------------------------------------------------------------------------

def contador(*num):
    tam = len(num)
    print(f'\nRecibi os valores {num}\n-> Ao todo são {tam}')

contador(2,3,4,5,4,2,1,)
contador(12344, 5666)
contador(3,3)

-------------------------------------------------------------------------

FUNÇÃO DE CALCULAR ÁREA

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terrreno {largura} x {comprimento} é de {a}m²')

a = float(input('Largura (m):'))
b = float(input('Comprimento (m):'))
area(a, b)

----------------------------------------------------------------------------------
   UM PRINT ESPECIAL

def escreva(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg} ')
    print('-' * tam)


escreva('Alyne Lima Meneses')
escreva('Matheus')

--------------------------------------------------------------------------------
  FUNÇÃO DE CONTADOR


from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = -passo

    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}:")

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont += passo
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont -= passo
    print("FIM!")
    print("-=" * 20)


# Programa Principal
# a) Contagem de 1 até 10 de 1 em 1
contador(1, 10, 1)

# b) Contagem de 10 até 0 de 2 em 2
contador(10, 0, 2)

# c) Contagem personalizada
print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)

--------------------------------------------------------------------------------
  FUNÇÃO QUE DESCOBRE O MAIOR

from random import randint

def sorteia(lista):
    print("Sorteando 5 números para a lista:", end=' ')
    for _ in range(5):
        num = randint(1, 100)  # Sorteia um número entre 1 e 100
        lista.append(num)
        print(num, end=' ')
    print("\nLista final:", lista)

def somaPar(lista):
    soma = sum(num for num in lista if num % 2 == 0)  # Soma apenas números pares
    print(f"Soma dos números pares da lista: {soma}")

# Programa Principal
numeros = []
sorteia(numeros)
somaPar(numeros)

---------------------------------------------------------------------------------------------

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3,4,6)
r2 = somar(2,3)
r3 = somar(1,2)
print(f'Meus calculos deram {r1}, {r2} e {r3}.')

----------------------------------------------------------------------

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA '
    elif 16 <= idade <18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO'


nas = int(input('Em que ano você nasceu?'))
print(voto(nas))

---------------------------------------------------------------

def factorial(n, show=False):
    """
    -> Calcula o Factorial de um numéro
    :param n:numéro a ser calculado
    :param show:(opcional) Mostar ou não a conta.
    :return:O valor do Factorial de um numéro n.
    """
    f= 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f += c
    return f

print(factorial(5, show=True))
help(factorial)

------------------------------------------------------------------------------

def ficha(jogador, gol):
    print(f'O(a) jogador(a) {jogador} fez {gol} gol(s) no campeonato.')

n = str(input('Nome do(a) Jogador(a): '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)

-----------------------------------------------------------------------------------

def Leia(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um número interio válido.\033[m')
        if ok:
            break
    return valor
n = Leia('Digite um numero:')
print(f'Voce acabou de digitar o numero {n}.')

----------------------------------------------------------------------------------

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
       if r['Média'] >= 7:
           r['Situação'] = 'BOA'
       elif r['Média'] >= 5:
           r['Situação'] = 'RAZOÁVEL'
       else:
           r['Situação'] = 'RUIM'
    return r


resp = notas(3,4,6 ,9, sit=True)
print(resp)
help(notas)

--------------------------------------------------------------------------------------

from time import sleep
c = ('\033[m',
     '\033[0;30;41',
     '\033[0;30;42',
     '\033[0;30;43',
     '\033[0;30;44',
     '\033[0;30;45',
     '\033[7;30');

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP ')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM!':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)

--------------------------------------------------------------------------------------

import uteis

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {uteis.dobro(num)} ')

#---------------------------------------------------------------














