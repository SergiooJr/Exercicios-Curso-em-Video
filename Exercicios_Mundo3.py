from ast import While
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

# for i in range(1, len(lista)+1, 2):
#     for i in lista:
#         print("\n", i, end=" ")

# exercicio 077
# palavras = ("aprender", "programar", "linguagem", "python", "curso", "gratis", "estudar", "praticar", "trabalhar", "mercado", "programador", "futuro")
# for i in palavras:
#     print(f"Na palavra {i.upper()} temos ", end="")
#     tuple(i)
#     for v in i:
#         if v in "aeiou":
#             print(v, end=" ")
#     print("\n")