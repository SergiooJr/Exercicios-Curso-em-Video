#                                   MUNDO 1
import os
import time
import datetime
import math
import random
os.system("cls")

# exercicio 003

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
#
# soma = num1 + num2
#
# print("A soma de {} + {} é {}".format(num1, num2, soma))

# exercicio 004
# algo = input("Digite algo: ")
# print("O tipo primitivo desse valor é: ", type(algo))
# print("Só tem espaços? ", algo.isspace())
# print("É um número? ", algo.isnumeric())
# print("É alfabético? ", algo.isalpha())
# print("É alfanumérico? ", algo.isalnum())
# print("Está em maiúculas? ", algo.isupper())
# print("Está em minúsculas? ", algo.islower())
# print("Está capitalizada? ", algo.istitle())

# exercicio 005
# a = int(input("Digite um número: "))
# print("Seu antecessor é: {} \nSeu sucessor é: {}".format(a-1, a+1))

# exercicio 006
# a = int(input("Digite um número: "))
# dobro = a*2
# triplo = a*3
# raizquadra = a**0.5  # ou "pow(a, 0.5)"
#
# print("O dobro de {} é: {} "
#       "\nO triplo é: {}"
#       "\nA raíz quadrada é {:.2f}"  # o ":.2f" significa duas casas decimais
#       .format(a, dobro, triplo, raizquadra))

# exercicio 007
# a = float(input("Digite a primeira nota: "))
# b = float(input("Digite a segunda nota: "))
# media = (a+b)/2
#
# print("Sua média é: ", media)

# exercicio 008
# a = float(input("Digite um valor em metros: "))
# centimetros = a*100
# milimetros = a*1000
#
# print("{} metros equilave à {} centimetros e {} milimetros".format(a, centimetros, milimetros))

# exercicio 009
# a = int(input("Digite um número para ver sua tabuada: "))
# print("{} X {:2} = {}".format(a, 1, a*1))  # o "{:2}" significa dois digitos p direita
# print("{} X {:3} = {}".format(a, 2, a*2))  # o "{:3}" significa três digitos p direita
# print("{} X {:5} = {}".format(a, 3, a*3))  # o "{:5}" significa cinco digitos p direita
# print("{} X {:1} = {}".format(a, 4, a*4))  # o "{:1}" significa um digito p direita
# print("{} X {:2} = {}".format(a, 5, a*5))
# print("{} X {:2} = {}".format(a, 6, a*6))
# print("{} X {:2} = {}".format(a, 7, a*7))
# print("{} X {:2} = {}".format(a, 8, a*8))
# print("{} X {:2} = {}".format(a, 9, a*9))
# print("{} X {:2} = {}".format(a, 10, a*10))

# exercicio 010
# a = float(input("Digite um valor em reais: "))
# dolar = a/3.27
#
# print("Você pode comprar {:.1f} dólares com {} reais".format(dolar,a))

# exercicio 011
# larg = float(input("Digite a largura da parede em metros: "))
# altu = float(input("Digite a altura da parede também em metros: "))
#
# area = larg*altu
#
# tinta = area/2
#
# print("A quantida de tinta é de {} litros de tinta".format(tinta))

# exercicio 012
# a = float(input("Digite o preço do produto: "))
# desconto = a*5/100
# novo = a-desconto  #ou "novo = a - (a*5/100)"
#
# print("O novo preço é de {} reais, com desconto de 5%".format(novo))

# exercicio 013
# a = float(input("Digite seu salario: "))
# aumento = a*15/100
# novo = a + aumento  # ou "novo = a + (a*15/100)"
#
# print("Com 15% de aumento, seu novo salario é de {} reais".format(novo))

# exercicio 014
# c = float(input("Informe a temperatura em °C: "))
# f = (c * 9)/5 + 32
# print("A temperatura de {}°C corresponde a {}°F".format(c, f))

# exercicio 015
# km = float(input("Informe a quantidade de Km percorridos: "))
# dias = int(input("Informe a quantidade de dias que o carro foi alugado: "))
#
# preco = (dias*60) + (km*0.15)
#
# print("O valor a pagar é de R$", preco)

# exercicio 016
# from math import trunc
# num = float(input("Digite um valor real: "))
# print("A parte inteira de {} é {}".format(num, trunc(num)))  # "trunc" pega a parte inteira de um numero

# ou

# num = float(input("Digite um valor real: "))
# print("A parte inteira de {} é {}".format(num, int(num)))

# exercicio 017
# catO = float(input("Informe o comprimento do cateto oposto: "))
# catA = float(input("Informe o comprimento do cateto adjacente: "))
#
# hip = (catO ** 2 + catA ** 2) ** 0.5
#
# print("O comprimento da hipotenusa é {:.2f}".format(hip))

# ou

# from math import hypot
# catO = float(input("Informe o comprimento do cateto oposto: "))
# catA = float(input("Informe o comprimento do cateto adjacente: "))
#
# hip = hypot(catO, catA)
#
# print("O comprimento da hipotenusa é {:.2f}".format(hip))

# exercicio 018
# from math import sin, cos, tan, radians
# ang = float(input("Digite o ângulo que você deseja: "))
#
# s = sin(radians(ang))  # "sin" retorna o seno em radiandos, "radians" transforma em radiando
# c = cos(radians(ang))  # "cos" retorna o cosseno em radiandos, "radians" transforma em radiando
# t = tan(radians(ang))  # "tan" retorna o tangente em radiandos, "radians" transforma em radiando
#
# print("O ângulo de {0:.2f} tem o SENO de {1:.2f}\nO ângulo de {0:.2f} tem o COSSENO de {2:.2f}\nO ângulo de {0:.2f}"
#       "tem a TANGENTE de {3:.2f}"
#       .format(ang, s, c, t))

# exercicio 019
# from random import choice
# a1 = str(input("Primeiro aluno: "))
# a2 = str(input("Segundo aluno: "))
# a3 = str(input("Terceiro aluno: "))
# a4 = str(input("Quarto aluno: "))
#
# lista = [a1, a2, a3, a4]
#
# escolhido = choice(lista)  # ecolhe algum elemento do vetor
#
# print("O aluno(a) escolhido(a) foi: {}".format(escolhido))

# exercicio 020
# from random import shuffle
# a1 = str(input("Primeiro aluno: "))
# a2 = str(input("Segundo aluno: "))
# a3 = str(input("Terceiro aluno: "))
# a4 = str(input("Quarto aluno: "))
#
# lista = [a1, a2, a3, a4]
#
# shuffle(lista)  # embaralha os elementos da lista
#
# print("A ordem de apresentação será\n{}".format(lista))

# exercicio 021
# import pygame
#
# pygame.mixer.init()  # iniciando o mixer
# pygame.init()  # iniciando o pygame
# pygame.mixer.music.load("ex_021_curto.mp3")  # carregando o arquivo mp3
# # pygame.mixer.music.play()  # dando play no arquivo
# pygame.mixer.music.play(loops=2, start=0.0)  # adicionando 2 loops no arquivo
# pygame.event.wait()  # espera o evento terminar p encerrar o programa

# exercicio 022
# nome = str(input("Digite seu nome completo: ")).strip()
# print("Seu nome completo com todas as letras maiusculas é: ", nome.upper())
# print("Seu nome completo com todas as letras minusculas é: ", nome.lower())
# print("Sem considerar espaços seu nome tem ao todo {} letras".format(len(nome)-nome.count(" ")))
# dividirNome = nome.split()
# print("Seu primeiro nome tem {} letras".format(len(dividirNome[0])))
#
# # ou
#
# print("Seu primeiro nome tem {} letras".format(nome.find(" ")))  # pois retorna a posição onde tem o primeiro " "

# exercicio 023
# numero = int(input("Digite um número: "))
# u = numero // 1 % 10
# d = numero // 10 % 10
# c = numero // 100 % 10
# m = numero // 1000
#
# print("Unidade: {}".format(u))
# print("Dezena: {}".format(d))
# print("Centena: {}".format(c))
# print("Milhar: {}".format(m))

# exercicio 024
# cidade = str(input("Digite o nome de uma cidade: ")).strip()
# print(cidade[:5].upper() == "SANTO")

# ou

# cidade = str(input("Digite o nome de uma cidade: "))
# divirCidade = cidade.split()
# if(divirCidade[0] == "Santo"):
#     print("Começa com Santo")
# else:
#     print("Não começa com Santo")

# exercicio 025
# nome = str(input("Digite seu nome: ")).strip()
# print("Seu nome tem Silva? {}".format("silva" in nome.lower()))

# ou

# nome = str(input("Digite seu nome: "))
# if("Silva" in nome):
#     print("Seu nome tem Silva")
# else:
#     print("Seu nome não tem Silva")

# exercicio 026
# frase = str(input("Digite uma frase: ")).upper().strip()
# print("A letra A aparece {} vezes na frase".format(frase.count("A")))
# print("A primeira letra apareceu na {} posição".format(frase.find("A")+1))
# print("A última letra apareceu na {} posição".format(frase.rfind("A")+1))

# exercicio 027
# n = str(input("Digite seu nome: ")).strip()
# nome = n.split()
# print("Primeiro nome: ", nome[0])
# print("Último nome: ", nome[len(nome)-1])

# exercicio 028
# from random import randint
# from time import sleep  # AGUARDEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
# numeroSorteado = randint(0, 5)
# print("O computador sorteou um numero entre 0 e 5, consegue adivinhar?\n")
# palpite = int(input("Digite seu palpite: "))
# print("Processando")
# sleep(2)  # esperar dois segundos
# if palpite == numeroSorteado:
#     print("Parabéns, você acertou!")
# else:
#     print("Infelizmente, você errou, ele pensou em {}, e não {}".format(numeroSorteado, palpite))

# exercicio 029
# velocidade = int(input("Informe a velocidade em Km/h: "))
# if velocidade > 80:
#     multa = (velocidade-80) * 7
#     print("Você foi mutado em {} reais".format(multa))
# else:
#     print("Você não foi multado")

# exercicio 030
# n = int(input("Digite um número inteiro: "))
# if n % 2 == 0:
#     print("Esse número é par")
# else:
#     print("Esse número é ímpar")

# exercicio 031
# distancia = float(input("Informe a distância da viagem em Km: "))
# if distancia < 200:
#     passagem = distancia * 0.50
#     print("O preço da passagem é {:.2f} reais".format(passagem))
# else:
#     passagem = distancia * 0.45
#     print("O preço da passagem é {:.2f} reais".format(passagem))

# exercicio 032
# from datetime import date
# ano = int(input("Informe o ano: "))
# if ano == 0:
#     ano = date.today().year  # vai pegar só o ano da data de hoje
# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#     print("Esse ano é bissexto")
# else:
#     print("Não é bissexto")

# exercicio 033
# num1 = float(input("Digite o 1° valor: "))
# num2 = float(input("Digite o 2° valor: "))
# num3 = float(input("Digite o 3° valor: "))
#
# maior = num1
# if num2 > num1 and num2>num3:
#     maior = num2
# if num3>num1 and num3>num2:
#     maior = num3
#
# print("{} é o maior".format(maior))
# menor = num1
# if num2<num1 and num2<num3:
#     menor = num2
# if num3<num1 and num3<num2:
#     menor = num3
# print("{} é o maior".format(menor))

# exercicio 034
# salario = float(input("Informe seu salário: "))
# if salario > 1250:
#     print("Com aumento de 10%, seu novo salário é de {} reias".format(salario+(salario*10/100)))
# else:
#     print("Com aumento de 15%, seu novo salário é de {} reais".format(salario+(salario*15/100)))

# exercicio 035
'''print("Analisador de trinagulos")
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar um triângulo!")
else:
    print("Os segmentos acima não podem formar um trinângulo!") '''