'''
Exercício: sortear um de quatro alunos, lendo o nome dos
alunos e escrevendo na tela o nome do escolhido.
'''

from random import choice

nome1 = str(input('Digite o primeiro nome: '))
nome2 = str(input('Digite o segundo nome: '))
nome3 = str(input('Digite o terceiro nome: '))
nome4 = str(input('Digite o quarto nome: '))


lista = [nome1,nome2,nome3,nome4]

escolha = choice(lista)

print('O nome escolhido foi {}  '.format(escolha))