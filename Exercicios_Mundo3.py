import os
import time
import datetime
import math
import random
os.system("cls")
#                                                  TUPLAS
# exercicio 072
# unidade = ("", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove")
# dezena = ("", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove")

# while True:
#     os.system("cls")
#     n = int(input("Digite um valor entre 0 e 20: "))
#     while n < 0 or n > 20:
#         print("Valor inválido!")
#         n = int(input("Digite um valor entre 0 e 20: "))
#     if n == 0:
#         print("zero")
#     if n == 20:
#         print("vinte")
#     d = n // 10
#     u = n % 10
#     if d == 1:
#         print(dezena[u])
#     else:
#         print(unidade[u])
#     resp = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
#     while resp not in "SN":
#         print("Opção inválida!")
#         resp = str(input("Apenas S ou N: ")).strip().upper()[0]
#     if resp == "N":
#         break

# exercicio 073
# times = ("", "Palmeiras", "Corinthias", "Internacional", "Atlético-MG", "Fluminense", "Athletico-PR", "São Paulo", "Santos", "Flamengo", "Botafogo", "Bragantino", "Goiás", "Cuiabá", "Coritiba"  "América-MG", "Avaí", "Ceará-SC", "Atlético-GO", "Juventude", "Fortaleza")

# print(f"OS 5 primeiros colocados são o: {times[0:5]}")
# print(f"Os 4 útimos colocados são o {times[-5:]}")
# print(f"Os times em ordem alfabética fica assim: {sorted(times)}")
# for i in range(len(times)):
#     if times[i] == "Bragantino":
#         print(f"O Bragantino está na {i}° posição da tabela")

# exercicio 074
# valores = tuple(random.randint(1, 10)for i in range(1, 6))
# print(f"Os valores digitados foram: {valores}")
# print(f"O maior valor digitado foi {max(valores)}")
# print(f"O menor valor digitado foi {min(valores)}")
# #                                                   OU
# a = tuple(random.sample(range(10), 5)) # o "sample" sorteia valores (1° parâmetro) e (2° parâmetro) a quantidade de vezes (como um looping) 
# print(a)
# print(f'O maior valor é {max(a)} e o menor é {min(a)}.')

# exercicio 075
# cont = 0
# valores = tuple(int(input("Digite os valores: "))for i in range(1, 5))
# print(f"O 9 apareceu {valores.count(9)} vezes")
# if 3 in valores:
#     print(f"O 3 foi digitado primeiramente na {valores.index(3)+1}° posição")
# else:
#     print("O três não foi digitado")
# print("Os valores pares são o ", end="")
# for i in valores:
#     if i % 2 == 0:
#         print(i, end=" ")
# #                               OU (com menos linhas)
# valores = tuple(int(input('Digite valores '))for c in range(1, 5))
# print(f'O numero nove aparece {valores.count(9)} vezes')
# print(f'Valor 3 foi digitado pela primeira vez na {valores.index(3)+1}º posição' if 3 in valores else 'Não foi digitado valor 3')
# print('Valores pares digitados foram', end=' ')
# print({n for n in valores if n % 2 == 0}, end=' ')

# exercicio 076
# lista = ("Lápis", 1.75, "Borracha", 2.00, "Cardeno", 15.90, "Estojo", 25.00, "Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

# print("-"*30)
# print(f'{"LISTAGEM DE PREÇOS":^30}') # ":^30" 30 caracteres centralizado
# print("-"*30)
# for i in range(0, len(lista)):
#     if i % 2 == 0:
#         print(f"{lista[i]:.<30}", end="") # ":.<30" 30 pontos alinhados a esquerda
#     else:
#         print(f"R${lista[i]:>7}")

# exercicio 077
# palavras = ("aprender", "programar", "linguagem", "python", "curso", "gratis", "estudar", "praticar", "trabalhar", "mercado", "programador", "futuro")
# for i in palavras:
#     print(f"Na palavra {i.upper()} temos ", end="")
#     for letra in i:
#         if letra in "aeiou":
#             print(letra, end=" ")
#     print("\n")

#                                                   LISTAS(pt-1)
# exercicio 078
# lista = list()
# maior = 0
# menor = 0
# for i in range(0, 5):
#     lista.append(int(input(f"Digite um valor para a Posição {i}: ")))
#     if i == 0:
#         maior = menor = lista[i]
#     if maior < lista[i]:
#         maior = lista[i]
#     elif menor > lista[i]:
#         menor = lista[i]
# print(f"\nO maior valor digitado foi: {maior} nas posições ", end="")
# for p, v in enumerate(lista):
#     if v == maior:
#         print(f"{p} ", end="")
# print(f"\nO menor valor digitado foi: {menor} nas posições ", end="")
# for p, v in enumerate(lista):
#     if v == menor:
#         print(f"{p} ", end="")

#                                   OU

# lista = list(int(input(f"Digite um valor para a Posição {i}: "))for i in range (0, 5))
# maior = max(lista)
# menor = min(lista)
# print(f"\nO maior valor digitado foi: {maior} nas posições ", end="")
# for p, v in enumerate(lista):
#     if v == maior:
#         print(f"{p}... ", end="")
# print(f"\nO menor valor digitado foi: {menor} nas posições ", end="")
# for p, v in enumerate(lista):
#     if v == menor:
#         print(f"{p}... ", end="")
# print(lista)

# exercicio 079
# valores = []
# while True:
#     escolha = " "
#     valor = int(input("Valor: "))
#     if valor not in valores:
#         valores.append(valor)
#         print("Adicionando valor...")
#     else:
#         print("Valor já existente na lista, não vou adicioná-lo")
#     while escolha not in "SN":
#         escolha = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
#     if escolha == "N":
#         break
# valores.sort()
# print(f"Você digitou os valores {valores}") 

# exercicio 080
# numeros = []
# for i in range(1, 6):
#     num = int(input("Digite um valor: "))
#     if i == 1 or num > numeros[-1]:
#         numeros.append(num)
#         print("Número adicionado na última posição.")
#     else:
#         for pos, val in enumerate(numeros):
#             if num <= val:
#                 print(f"Adicionado na {pos} posição da lista.")
#                 numeros.insert(pos, num)
#                 break
# print(f"{numeros}")  

# exercicio 081
# numeros = []
# while True:
#     escolha = " "
#     numeros.append(int(input("Digite um valor: ")))
#     while escolha not in "SN":
#         escolha = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
#     if escolha == "N":
#         break
# print(f"Foram digitados {len(numeros)} números")
# numeros.sort(reverse=True)
# print(f"A lista de valores em ordem decrescente é {numeros}")
# if 5 in numeros:
#     print("O valor 5 está na lista. Nas posições: ", end="")
# numeros.sort() # coloquei isso, pois sem isso, o numero maior ficava na posição zero smp, tire e teste
# for posi, val in enumerate(numeros):
#     if val == 5:
#         print(posi, end=" ")
# if 5 not in numeros:
#     print("O valor 5 não está na lista")

# exercicio 082
# valores = []
# valoresP = []
# valoresI = []
# while True:
#     escolha = " "
#     num = int(input("Digite um valor: "))
#     valores.append(num)
#     if num % 2 == 1:
#         valoresI.append(num)
#     else:
#         valoresP.append(num)
#     while escolha not in "SN":
#         escolha = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
#     if escolha == "N":
#         break
# print(f"Lista cheia: {valores} \n Lista pares: {valoresP} \n Lista ímpares: {valoresI}")

# exercicio 083
# ERRADO
# expr = str(input("Digite a expressão: "))
# abertos = []
# fechados = []
# for i in expr:
#     print(i)
#     if i == "(":
#         abertos.append("(")
#     elif i == ")":
#         fechados.append(")")
# if len(abertos) == len(fechados):
#     print("Sua expressão é válida")
# else:
#     print("Sua expressão é inválida")
# CORRETO
# lista = []
# expr = str(input("Digite a expressão: "))
# for simb in expr:
#     if simb == "(":
#         lista.append("(")
#     elif simb == ")":
#         if len(lista)>0:
#             lista.pop()
#         else:
#             lista.append(")")
#             break
# if len(lista) == 0:
#     print("Sua expressão está válida!")
# else:
#     print("Sua expressão está inválida!")
#                                                   LISTAS(pt-2)
# exercicio 084
# temp = []
# princ = []
# pMaior = pMenor = 0
# while True:
#     resp = " "
#     temp.append(str(input("Nome: ")))
#     temp.append(int(input("Peso: ")))
#     if len(princ) == 0:
#         pMaior = pMenor = temp[1]
#     else:
#         if temp[1] > pMaior:
#             pMaior = temp[1]
#         if temp[1] < pMenor:
#             pMenor = temp[1]
#     princ.append(temp[:])
#     temp.clear()
#     while resp not in "SN":
#         resp = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
#     if resp == "N":
#         break
# print("="*20)
# print(f"Foram cadastradas {len(princ)} princ.")
# print(f"O maior peso foi de {pMaior}Kg. Peso de ", end="")
# for p in princ:
#     if p[1] == pMaior:
#         print(f"[{p[0]}]", end=" ")
# print(f"\nO menor peso foi {pMenor}Kg. Peso de ", end="")
# for p in princ:
#         if p[1] == pMenor:
#             print(f"[{p[0]}]", end=" ")

# exercicio 085
# lista = [[], []]
# p = 0
# for i in range(1, 8):
#     valor = int(input(f"Digite o {i}° Valor: "))
#     if valor % 2 == 0:
#         lista[0].append(valor)
#     else:
#         lista[1].append(valor)
# lista[0].sort()
# lista[1].sort()
# print(f"Todos os valores pares digitados foram {lista[0]}")
# print(f"Todos os números ímpares digitados foram {lista[1]}")

# exercicio 086
# matriz = [[0, 0, 0,], [0, 0, 0], [0, 0, 0]]
# for l in range(0, 3): # linha
#     for c in range(0, 3): # coluna
#         matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
# print("-="*20)
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f"[{matriz[l][c]:^5}]", end="") # ":^5" é p ficar centralizado em cinco espaços
#     print("")

# exercicio 087
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# somaP = somaT = mSeg = 0
# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
# print("=-="*20)
# for l in range(0, 3):
#     somaT += matriz[l][2]
#     for c in range(0, 3):
#         print(f"[{matriz[l][c]:^3}]", end="")
#         if matriz[l][c] % 2 == 0:
#             somaP += matriz[l][c]
#         #             OU
#         # if c == 2:
#         #     somaT += matriz[l][c]
#         if l == 1 and c == 0:
#             mSeg = matriz[1][c]
#         else:
#             if matriz[1][c] > mSeg:
#                 mSeg = matriz[1][c]
#     print()
# print("-=-"*20)
# print(f"A soma dos números pares é: {somaP}")
# print(f"A soma dos valores da terceira coluna é: {somaT}")
# print(f"O maior valor da segunda linha é: {mSeg}")

# exercicio 088
# from random import randint
# lista = []
# jogos = []
# cont = contV = total = 0
# print("-"*30)
# print("JOGA NA MEGA SENA".center(29)) # centraliza a string em 29 espaços
# print("-"*30)
# vezes = int(input("Quantos jogos você quer que eu sorteie? "))
# while total < vezes:
#     cont = 0
#     while True:
#         valores = randint(1, 60)
#         if valores not in lista:
#             lista.append(valores)
#             cont += 1
#         if cont >= 6:
#             break
#     lista.sort()
#     jogos.append(lista[:])
#     lista.clear()
#     total += 1
# for p, v in enumerate(jogos):
#     print(f"Jogo {p+1}: {v}")
#     time.sleep(1)
# print(f"\033[32mBOA SORTE!".center(29))
# print("\033[m")
#                                   SEM USAR LISTA COMPOSTA
# jogo = []
# quant = int(input('Quer gerar quantos jogos? '))
# for i in range(0, quant):
#     while len(jogo) < 6:
#         n = random.randint(1, 60)
#         if n not in jogo:
#             jogo.append(n)
#     print(f'Jogo {i+1}: {sorted(jogo)}')
#     time.sleep(1)

# exercicio 089

