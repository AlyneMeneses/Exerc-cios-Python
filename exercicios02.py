
#---------------------------------------------------------------------------------------------------------------

# DEIXE SEU NOME TODO EM MAIUSCULO OU EM MINUSCULO E AINDA SOMA O TOTAL DE LETRAS NO SEU RPIMEIRO NOME.

nome_completo = str(input('digite seu nome completo:'))

print('nome em maiusculo:', nome_completo.upper())
print('nome em minusculo:', nome_completo.lower())
nome_sem_espaco = nome_completo.replace(' ', '')
print('número total de letras (sem espaço):',len(nome_sem_espaco))
primeiro_nome = nome_completo.split()[0]
print('números de letras do primeiro nome:', len(primeiro_nome))

#------------------------------------------------------------------------------------------------------------

#UNIDADE, DEZENA, CENTENA E MILHAR DE UM NUMERO

numero = int(input('informe um numero:'))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'unidade:{unidade}')
print(f'dezena:{dezena}')
print(f'centena:{centena}')
print(f'milhar:{milhar}')

#--------------------------------------------------------------------------------------------------------


# LER O NOME COMPLETO E VERIFICAR SE ELA TEM TAL SOBRENOME.

nome = input('digite seu nome completo:')

if "meneses" in nome.lower():
    print("O nome contém 'meneses'.")
else:
    print("Nao contém 'meneses' ")

#-----------------------------------------------------------------------------------------------
# VERIFICA DE TAL LETRA APARECEU NA FRASE, MOSTRA A POSIÇÃO EM QUE ELA ESTÁ.

frase = str(input('digite uma frase:')).strip()
l = frase.lower()
print('a letra A aparece vezes na frase', l.count('a'))
print('a primeira letra A aparece na posiçao:', l.find('a')+1)
print('a ultima A aparece na posiçao:', l.rfind('a')+1)

#-----------------------------------------------------------------------------------

# MOSTRA O PRIMEIRO E ULTIMO NOME

n = str(input('nome completo:')).strip()
nome = n.split()
print('seu primeiro nome é:', nome[0])
print('seu ultimo nome é:', nome[len(nome)-1])