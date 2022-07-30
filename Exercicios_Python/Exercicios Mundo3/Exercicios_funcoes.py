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
#     print(f'  {msg}')
#     print('~'*len(msg))
# escreva('Gustavo Guanabara')
# escreva('Curso de Python no Youtube')
# escreva('CeV')

# exercicio 098
# def contador(i, f, p):
#     if p<0:
#         p*=-1
#            OU
# #        p = abs(p) (tranforma o numero em positivo)
#     if p == 0:
#         p = 1
#     if i>f:
#         print(f'Contagem de {i} até {f} de {p} em {p}')
#         for c in range(i, f-1, -p):
#             time.sleep(0.5)
#             print(c, end=" ")
#         print()
#     else:
#         print(f'Contagem de {i} até {f} de {p} em {p}')
#         for c in range(i, f+1, p):
#             time.sleep(0.5)
#             print(c, end=" ")
#         print()
# contador(1, 10, 1)
# contador(10, 0, 2)
# print('Agora é sua vez de personalizar a contagem!')
# contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))

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
# exercicio 101
# def voto(dNasc):
#     anoA = datetime.date.today().year
#     idade = anoA - dNasc
#     if idade < 16:
#         print(f"Com {idade} anos: NÃO VOTA.")
#     elif idade < 18 or idade > 64:
#         print(f"Com {idade} anos: VOTO OPCIONAL.")
#     else:
#         print(f"Com {idade} anos: VOTO OBRIGATÓRIO")
# nasc = int(input("Em que ano você nasceu? "))
# voto(nasc)
#                           OU
# def voto(dNasc):
#     anoA = datetime.date.today().year
#     idade = anoA - dNasc
#     if idade < 16:
#         return f"Com {idade} anos: NÃO VOTA."
#     elif idade < 18 or idade > 64:
#         return f"Com {idade} anos: VOTO OPCIONAL."
#     else:
#         return f"Com {idade} anos: VOTO OBRIGATÓRIO"
# nasc = int(input("Em que ano você nasceu? "))
# print(voto(nasc))

# exercicio 102
# def fatorial(num=0, show=False):
#     """
#     -> Calcula o fatorial de um numero.
#         - param num: O numero a ser calculado.
#         - param show: (opcional) Mostrar ou nao a conta.
#         - return: O valor do fatorial de num.
#     Funcao criada por Sergio Junior.
#     """
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#         if show == True:
#             print(f"{c} x ", end="")
#     print("= ", end="")
#     return f
# print(fatorial(5, show=True))
# help(fatorial)

# exercicio 103
# def ficha(nome="", gols=""):
#     if nome == "":
#        print(f"O jogador <desconhecido> fez {gols} gol(s) no campeonato.")
#     elif gols == "":
#          print(f"O jogador {nome} fez 0 gols no campeonato.")
#     elif nome == "" and gols == "":
#         print(f"O jogador <desconhecido> fez 0 gols no campeonato.")
#     else: 
#         print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")
# ficha(str(input("Nome do jogador: ")).strip(), str(input("Número de gols: ")).strip())

# exercicio 104
# def leiaInt(num):
#     ok = False
#     valor = 0
#     while True:
#         r = str(input(num))
#         if r.isnumeric():
#             valor = int(r)
#             ok = True
#         else:
#             print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")
#         if ok:
#             return valor

# n = leiaInt('Digite um número: ')
# print(f'Você acabou de digitar o número {n}')

# exercicio 105
# def notas (*n, sit=False):
#     """
#     -> Função para analisar notas e situações de vários alunos.
#         - param n: uma ou mais notas dos alunos
#         - param sit: valor opcional, indicando se deve ou não adicionar a situação
#         - return: dicionário com várias informações sobre a situação do aluno/turma.
#     """
#     dados = dict()
#     dados["total"] = len(n)
#     dados["maior"] = max(n)
#     dados["menor"] = min(n)
#     dados["media"] = (f"{sum(n)/len(n):.1f}")
#     if sit:
#         if float(dados["media"]) >= 7:
#             dados["situação"] = "BOA"
#         elif dados["media"] >= 5:
#             dados["situação"] = "RAZOÁVEL"
#         else:
#             dados["situação"] = "RUIM"
#     return dados
# resp = notas(5.5, 9.5, 10, 6.5, sit=False)
# print(resp)

# exercicio 106
# c = ("\033[m",           # 0 -sem cores
#      "\033[0;30;41m",    # 1 - vermelho
#      "\033[0;30;42m",    # 2 - verde
#      "\033[0;30;43m",    # 3 - amarelo
#      "\033[0;30;44m",    # 4 - azul
#      "\033[0;30;45m",    # 5 - roxo
#      "\033[7;30m");      # 6 - branco

# def ajuda(com):
#     titulo(f"Acessando o manual do comando \"{com}\"", 4)
#     print(c[6], end="")
#     help(com)
#     print(c[0], end="")
#     time.sleep(2)

# def titulo(msg, cor=0):
#     tam = len(msg) + 4
#     print(c[cor], end="")
#     print("~"*tam)
#     print(f"{msg}")
#     print("~"*tam)
#     print(c[0], end="")
#     time.sleep(1)
# comando = ""
# while True:
#     titulo("SISTEMA DE AJUDA PyHELP", 2)
#     comando = str(input("Função ou Biblioteca > "))
#     if comando.upper() == "FIM":
#         break
#     else:
#         ajuda(comando)
# titulo("ATÉ LOGO!", 1)