#                                                       FUNÇÕES
import os
import time
import datetime
import math
import random
os.system("cls")

# exercicio 096
# def area(l, c):
#     r = l * c
#     print(f'A área de um terreno {l:.1f}x{c:.1f} é de {r:.1f}m².')

# print('CONTROLE DE TERRENOS')
# print('-'*20)
# area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))

# exercicio 097
# def escreva(msg):
#     print("~"*len(msg))
#     print(msg)
#     print('~'*len(msg))
# escreva('Gustavo Guanabara')
# escreva('Curso de Python no Youtube')
# escreva('CeV')

# exercicio 098


# exercicio 099
# def maior(*valores):
#     maior = 0
#     print('-='*50)
#     print('Analisando os valores passados...')
#     for v in valores:
#         if v == 0:
#             maior = v
#         if maior < v:
#             maior = v
#         print(f'{v} ', end='')
#         sleep(0.5)
#     print(f'Foram informados {len(valores)} valores ao todo.')
#     print(f'O maior valor informado foi {maior}.')

# maior(2, 9, 7, 4, 1)
# maior(4, 7, 0)
# maior(1, 2)
# maior(6)
# maior()

# exercicio 100
# numeros = []
# def sorteia():
#     print('Sorteando 5 valores da lista: ', end='')
#     for i in range(0, 5):
#         r = random.randint(1, 10)
#         numeros.append(r)
#         print(r, end=' ')
#     print('PRONTO!')
# def somaPar(valor):
#     soma = 0
#     print(f'Somando os valores pares de {valor}, temos ', end='')
#     for i in valor:
#         if i % 2 == 0:
#             soma += i
#     print(soma)
# sorteia()
# somaPar(numeros)

#                                                       FUNÇÕES-pt2
