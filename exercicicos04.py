

#-----------------------------------------------------------------------------

# SIMULAÇÃO DE UM EMPRESTIMO PARA COMPRAR UMA CASA

valor_casa = float(input('digite o valor da casa:'))
salario = float(input('digite o salario:'))
anos = float(input('digite em quantos anos pretende pagar:'))

meses = anos * 12
prestacao_mensal = valor_casa / meses
limite = salario * 0.3

print(f'\nValor da prestação mensal:{prestacao_mensal:.2f}')
print(f'Limite permitido: R${limite:.2f}')

if prestacao_mensal <= limite:
    print('\033[32m Emprestimo aprovado!!!!\033[32m')
else:
    print('\033[31:4m->Emprestimo negado! A prestaçao excede 30% do salário. \033[31:4m')


#-----------------------------------------------------------------------------------

# CONVERTE UM NUMERO PARA BINÁRIO, OCTAL OU HEXADECIMAL.

n = int(input('digite um número interio:'))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')

opcao = int(input('\033[34mSua opção:\033[34m'))
if opcao == 1:
    print(f'\033[33m{n} convertido para Binário é igual a {bin(n)[2:]}\033[33m')
elif opcao == 2:
    print(f'\033[33m{n} convertido para Binário é igual a {oct(n)[2:]}\033[33m')
elif opcao == 3:
    print(f'\033[33m{n} convertido para Binário é igual a {(hex(n)[2:])}\033[33m')
else:
    print('\033[33mNão existe esta opção. Tente novamente.\033[33m')


#--------------------------------------------------------------------------------------

# DIGITE DOIS NUMEROS E ESTE CODIGO IRA MOSTRAR QUAL O MAIOR OU MENOR E SE FOREM IGUAIS.

n1 = int(input('primeiro numero:'))
n2 = int(input('segundo numero:'))
if n1 > n2:
    print('O primeiro número é maior.' )
elif n2 > n1:
    print('O segundo número é maior.' )
else:
    print('Os dois números são \033[33miguais.')


#--------------------------------------------------------------------------------

# ALISTAMENTO PARA O EXERCITO: DIGITE SUA IDADE.

from datetime import date
atual = date.today().year

nasc = int(input('Em que ano você nasceu?'))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('Você tem que se alistar imediatamente.')
elif idade < 18:
    saldo = idade - 18
    print(f'Voce ainda nao tem 18 anos ainda falta {saldo} anos para o alistamento.')
elif idade > 18:
    saldo = idade - 18
    print(f'Voce ja deveria ter se alistado há {saldo} anos.')

#--------------------------------------------------------------------------------------------

# DIGITE SUAS NOTAS E IRÁ MOSTRA SUA MÉDIA E SE VOCE PASSOU OU FICOU DE RECUPERAÇÃO.

n1 = float(input('primeira nota:'))
n2 = float(input('segunda nota:'))

media = (n1 + n2) / 2
print(f'tirando {n1} e {n2}, a média será {media:.1f}')

if 7 > media >= 5:
    print('\033[31m RECUPERAÇÃO \033[31m')
elif media < 5:
    print('\033[31m REPROVADO \033[31m')
else:
    print('\033[34m APROVADO \033[34m')

#-----------------------------------------------------------------------------

# AQUI MOSTRA A CLASSIFICAÇÃO DE UM ATLETA DE ACORDO COM A IDADE DELE.

from datetime import date

atual = date.today().year
nasc = int(input('Ano de Nascimento:'))
idade = atual - nasc
print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('\033[34mClassificação MIRIM.')
elif idade <= 14:
    print('\033[34mClassificação INFANTIL.')
elif idade <= 19:
    print('\033[34mClassificação JUNIOR.')
elif idade <= 25:
    print('\033[34mClassificação SÊNIOR.')
else:
    print('\033[34mClassificação MASTER.')

#-------------------------------------------------------------------------------------------

# MOSTRA SE OS SEGMENTOS PODEM FORMAR UM TRIANGULO

r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima, PODEM FORMAR triângulo', end='')
    if r1 == r2 and r2 == r3:
        print('\033[34m EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('\033[34m ESCALENO')
    else:
        print('\033[34m ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo.')


#-----------------------------------------------------------------------------------

# MOSTRA O "IMC" DE UMA PESSOA

peso = float(input('Qual é seu peso? (Kg)'))
altura = float(input('Qual sua altura? (m)'))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')

if imc < 18.5:
    print('\033[34m ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('\033[34m PESO IDEAL')
elif 25 <= imc < 30:
    print('\033[34m SOBREPESO')
elif 30 <= imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')


#---------------------------------------------------------------------------------

# UM MERCADINHO

print((25 * '\033[34m='), ('ALYNE VENDAS'), (25 * '=\033[34m'))

preco = float(input('\033[32:1m Preco das compras:'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] á vista (dinheiro/cheque)
[ 2 ] á vista cartão
[ 3 ] 2x no cartão''')
opcao = int(input('Qual opção?'))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 /100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
print(f'\033[34mGANHOU DESCONTO!! Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')


#-----------------------------------------------------------------------------------

# ESTE É LEGAL
# É UM JOGO DE PEDRA, PAPEL OU TESOURA

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)

print('-=' * 12)
print(f'Voce escolheu {itens[jogador]}')
print(f'Computador jogou {itens[comp]}')
print('-=' * 12)

if comp == 0:
    if jogador == 0:
        print('\033[31mDEU EMPATE!')
    elif jogador == 1:
        print('\033[34mVOCÊ VENCEU')
    elif jogador == 2:
        print('\033[31mA maquina VENDEU de você')
    else:
        print('JOGADA INVALIDA!')

elif comp == 1:
    if jogador == 0:
        print('\033[31mA maquina VENCEU')
    elif jogador == 1:
        print('\033[31mDEU EMPATE')
    elif jogador == 2:
        print('\033[34mVOCÊ VENDEU')
    else:
        print('JOGADA INVALIDA!')
elif comp == 2:
    if jogador == 0:
        print('\033[34mVOCÊ VENCEU')
    elif jogador == 1:
        print('\033[31mA maquina VENCEU')
    elif jogador == 2:
        print('\033[31m-->DEU EMPATE')
    else:
        print('JOGADA INVALIDA!')

