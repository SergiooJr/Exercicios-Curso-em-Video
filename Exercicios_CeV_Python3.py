from operator import truediv
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

# exercicio 036
# valorCasa = float(input("Valor da casa: R$"))
# salario = float(input("Salário do comprador: R$"))
# anosFinan = int(input("Quantos anos de financiamento? "))

# meses = anosFinan*12
# parcela = valorCasa/meses

# print("Para pagar uma casa de {:.2f} em {} anos a prestação será de {:.2f}".format(valorCasa, anosFinan, parcela))

# if parcela > (salario*30/100):
#     print("Empréstimo NEGADO!")
# else:
#     print("Empréstimo APROVADO!")

# exercicio 037
# num = int(input("Digite um número inteiro: "))
# print('''Escolha uma das bases para conversão
# [1] converter para BINÁRIO
# [2] converter para OCTAL
# [3] converter para HEXADECIMAL''')
# opcao = int(input("Sua opção: "))
# if opcao == 1:
#     print("{} convertido para BINÁRIO é igual a {}".format(num, bin(num)[2:]))
# elif opcao == 2:
#     print("{} convertido para OCTAL é igual a {}".format(num, oct(num)[2:]))
# elif opcao == 3:
#     print("{} convertido para HEXADECIMAL é igual a {}".format(num, hex(num)[2:]))
# else:
#     print("Opção inválida! Tente novamente")

# exercicio 038
# num1 = float(input("Primeiro número: "))
# num2 = float(input("Segundo número: "))

# if num1>num2:
#     print("O PRIMEIRO valor é maior")
# elif num2>num1:
#     print("O SEGUNDO valor é maior")
# else:
#     print("Os valores são IGUAIS")

# exercicio 039
# from datetime import date
# anoNasc = int(input("Ano de nascimento: "))
# anoAtual = date.today().year
# idade = anoAtual - anoNasc
# print("Quem nasceu em {} tem {} anos em {}".format(anoNasc, idade, anoAtual))
# if idade < 18:
#     print("Ainda faltam {} para o alistamento".format(18-idade))
#     print("Você deve se alistar em {}".format(anoAtual + (18-idade)))
# elif idade > 18:
#     print("Você deveria já ter se alistado há {} anos".format(idade-18))
#     print("Seu alistamento foi em {}".format(anoAtual-(idade-18)))
# else:
#     print("Você de ve se alistar já!")

# exercicio 040
# n = float(input("Primeira nota: "))
# n2 = float(input("Segunda nota: "))
# media = (n+n2)/2
# print("Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f} ".format(n, n2, media))
# print("O aluno está ", end="")
# if media < 5:
#     print("REPROVADO!")
# elif 6.9>media>=5:
#     print("em RECUPERAÇÃO!")
# else:
#     print("APROVADO!")

# exercicio 041 PEGANDO A DATA DO SISTEMA
# from datetime import date
# atual = date.today().year
# nascimento = int(input("Ano de nascimento: "))
# idade = atual - nascimento
# print("O atleta tem {} anos.".format(idade))
# if idade <= 9:
#     print("Classificação: MIRIM")
# elif idade <= 14:
#     print("Classificação: INFANTIL")
# elif idade <= 19:
#     print("Classificação: JUNIOR")
# elif idade <= 25:
#     print("Classificação: SÊNIOR")
# else:
#     print("Classificação: MASTER")

# exercicio 042
# r1 = float(input("Primeiro segmento: "))
# r2 = float(input("Segundo segmento: "))
# r3 = float(input("Terceiro segmento: "))

# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r3:
#     print("Os segmentos acima PODEM formar um triângulo ", end="")
#     if r1 == r2 == r3:
#         print("EQUILÁTERO")
#     elif r1 != r2 != r3 != r1:
#         print("ESCALENO")
#     else:
#         print("ISÓCELES")
# else:
#     print("Os segmentos acima NÃO podem formar um triângulo")

# exercicio 043
# peso = float(input("Qual seu peso? (Kg) "))
# altura = float(input("Qual a sua altura? (m) "))
# imc = peso / (altura**2)
# print("O imc desta pessoa é {:.1f}".format(imc))
# if imc<18.5:
#     print("Você está abaixo do peso normal")
# elif imc<25:
#     print("Você está no peso ideal")
# elif imc<30:
#     print("Você está com sobrepeso")
# elif imc<40:
#     print("Você está obeso")
# else:
#     print("Você tem obesidade mórbida")

# exercicio 044
# print("="*10, "LOJAS AUGUSTO", "="*10)
# valor = float(input("Preço das compras: R$"))
# print("FORMAS DE PAGAMENTO")
# print("[1] à vista dinheiro/cheque")
# print("[2] à vista cartão")
# print("[3] 2x no cartão")
# print("[4] 3x ou mais no cartão")
# opcao = int(input("Qual é a opção? "))
# if opcao == 1:
#     print("Sua compra de R${:.2f}, vai custar R${:.2f} no final".format(valor, valor - (valor*10/100)))
# elif opcao == 2:
#     print("Sua compra de R${:.2f}, vai custar R${:.2f} no final".format(valor, valor - (valor*5/100)))
# elif opcao == 3:
#     print("Sua compra vai custar R${:.2fvalor}")
# elif opcao == 4:
#     vezes = int(input("Quantas parcelas? "))
#     print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS".format(vezes, valor/vezes + (valor/vezes)*20/100))
#     print("Sua compra de R${:.2f}, vai custar R${:.2f} no final".format(valor, valor + (valor*20/100)))
# else:
#     print("Opção inválida!")

# exercicio 045                             SEM PLACAR
# from random import randint
# from time import sleep

# print('''Suas opções:
# [0] PEDRA
# [1] PAPEL
# [2] TESOURA''')
# escolha = int(input("Qual é sua jogada? "))

# if escolha != 0 and escolha != 1 and escolha != 2:
#     print("Opção inválida! Tente novamente :)")
# else:
#     print("JO")
#     sleep(1)
#     print("KEN")
#     sleep(1)
#     print("PO!!!")
#     print("-="*20)

#     itens = ("Pedra", "Papel", "Tesoura")
#     computador = randint(0,2)
#     escolhaComput = itens[computador]
#     escolhaJog = itens[escolha]

#     print("O computador escolheu {}".format(escolhaComput))
#     print("O jogador escolheu {}".format(escolhaJog))
#     print("-="*20)

#     if escolhaComput != escolhaJog:
#         if escolhaComput == "Pedra" and escolhaJog == "Papel" or escolhaComput == "Papel" and escolhaJog == "Tesoura" or escolhaComput == "Tesoura" and escolhaJog == "Pedra":
#             print("Jogador venceu!")
#         #                           OU
#         # elif escolhaComput == "Papel" and escolhaJog == "Tesoura":
#         #     print("Jogador venceu!")
#         # elif escolhaComput == "Tesoura" and escolhaJog == "Pedra":
#         #     print("Jogador venceu!")
#         else:
#             print("Computador venceu!")
#     else:
#         print("EMPATOU!")

# exercicio 045                             COM PLACAR
# from distutils.command.clean import clean
# from random import randint
# from time import sleep
# import os

# placarComp = 0
# placarJog = 0
# verifica = 0
# verifica2 = 0

# while verifica2 == 0:
#     verifica = 0
#     os.system("cls")
#     print('''Suas opções:
#     [0] PEDRA
#     [1] PAPEL
#     [2] TESOURA''')
#     escolha = int(input("Qual é sua jogada? "))

#     if escolha != 0 and escolha != 1 and escolha != 2:
#         print("Opção inválida! Tente novamente :)")
#         sleep(3)
#         os.system("cls")
#     else:
#         print("JO")
#         sleep(1)
#         print("KEN")
#         sleep(1)
#         print("PO!!!")
#         print("-="*20)

#         itens = ("Pedra", "Papel", "Tesoura")
#         computador = randint(0,2)
#         escolhaComput = itens[computador]
#         escolhaJog = itens[escolha]

#         print("O computador escolheu {}".format(escolhaComput))
#         print("O jogador escolheu {}".format(escolhaJog))
#         print("-="*20)

#         if escolhaComput != escolhaJog:
#             if escolhaComput == "Pedra" and escolhaJog == "Papel" or escolhaComput == "Papel" and escolhaJog == "Tesoura" or escolhaComput == "Tesoura" and escolhaJog == "Pedra":
#                 print("Jogador venceu!")
#                 placarJog = placarJog + 1
#                 print("Placar atualizado: {} (jogador) a {} (computador)".format(placarJog, placarComp))
#                 sleep(3)
#                 os.system("cls")
#                 if placarJog == 3:
#                     print("O GRANDE CAMPEÃO É O JOGADOR!")
#                     while verifica == 0:
#                         recomecar = str(input("Deseja recomeçar? (s/n) ").lower().strip())
#                         if recomecar == "s":
#                             print("Tudo bem, recomeçando...")
#                             sleep(0.5)
#                             print(".")
#                             sleep(0.5)
#                             print("..")
#                             sleep(0.5)
#                             print("...")
#                             sleep(1)
#                             placarComp = 0
#                             placarJog = 0
#                             verifica = 1
#                             verifica2 = 0
#                             os.system("cls")
#                         elif recomecar == "n":
#                             verifica = 1
#                             print("Tudo bem, até a próxima :)")
#                             sleep(1)
#                             verifica2 = 1
#                             os.system("cls")
#                         else:
#                             print("Opção inválida, apenas s/n!")
#                             sleep(3)
#                             verifica = 0
#                             os.system("cls")
#             else:
#                 print("Computador venceu!")
#                 placarComp = placarComp + 1
#                 print("Placar atualizado: {} (jogador) a {} (computador)".format(placarJog, placarComp))
#                 sleep(3)
#                 os.system("cls")
#                 if placarComp == 3:
#                     print("O GRANDE CAMPEÃO É O COMPUTADOR!\n")
#                     sleep(1)
#                     while verifica == 0:
#                         recomecar = str(input("Deseja recomeçar? (s/n) ").lower().strip())
#                         if recomecar == "s":
#                             print("Tudo bem, recomeçando...")
#                             sleep(0.5)
#                             print(".")
#                             sleep(0.5)
#                             print("..")
#                             sleep(0.5)
#                             print("...")
#                             sleep(1)
#                             placarComp = 0
#                             placarJog = 0
#                             verifica = 1
#                             verifica2 = 0
#                             os.system("cls")
#                         elif recomecar == "n":
#                             verifica = 1
#                             print("Tudo bem, até a próxima :)")
#                             sleep(1)
#                             verifica2 = 1
#                             os.system("cls")
#                         else:
#                             print("Opção inválida, apenas s/n!")
#                             sleep(3)
#                             verifica = 0
#                             os.system("cls")
#         else:
#             print("EMPATOU!")
#             print("Placar atualizado: {} (jogador) a {} (computador)".format(placarJog, placarComp))
#             sleep(3)
#             os.system("cls")
#                           COM EMOJIS :)
# import random
# import emoji
# from time import sleep
# emoj=[emoji.emojize(':victory_hand:'), emoji.emojize(':raised_hand:'), emoji.emojize(':raised_fist:')]
# maquina=random.choice(emoj)
# print('PEDRA')
# sleep(1)
# print('PAPEL')
# sleep(1)
# print('TESOURA...')
# sleep(1)
# print(maquina)

#                                       LAÇOS FOR

# exercicio 046
# from time import sleep
# import os

# os.system("cls")
# for i in range(10, 0, -1):
#     print(i)
#     sleep(1)

# exercicio 047
# import os

# os.system("cls")
# contador = 0
# for i in range(1, 51):
#     par = i%2
#     if par == 0:
#         print(i)
#                                       OU
# os.system("cls")
# for i in range(2, 51, 2):
#     print(i)

# exercicio #048
# import os

# os.system("cls")
# contador = 0
# for i in range(1, 501):
#     impar = i%2
#     multiplo3 = i%3
#     if impar == 1 and multiplo3 == 0:
#         contador += i
# print("{} números entre 1 e 500 são ímpares e multiplos de 3".format(contador))
#                                   OU
# os.system("cls")
# contador = 0
# for i in range(1, 501, 2):
#     multiplo3 = i%3
#     if multiplo3 == 0:
#         contador += i
# print("{} números entre 1 e 500 são ímpares e multiplos de 3".format(contador))

# exercicio 049
# import os

# os.system("cls")
# num = int(input("Digite um número para ver a tabuada: "))
# for i in range (1, 11):
#     print ("{} X {:2} = {}".format(num, i, (num*i)))

# exercicio 050

# os.system("cls")
# soma = 0
# for i in range (1, 7):
#     num = int(input("Digite um número inteiro: "))
#     if num%2 == 0:
#         soma += num
# print("A soma dos números pares digitados é de {}".format(soma))

# exercicio 051

# print("\033[33m="*20)
# print("\033[32m10 TERMOS DE UMA PA")
# print("\033[33m="*20,"\n")
# print("\033[m")
# pTermo = int(input("Primeiro termo: "))
# razao = int(input("Razão: "))
# decimo = pTermo + (10-1) * razao
# for i in range(pTermo, decimo, razao):
#     print(i, end=" → ");
# print("\033[31mACABOU")
# print("\033[m")

# exercicio 052

# os.system("cls")
# qnt = 0
# num = int(input("Digite um valor: "))
# for i in range(1, num+1):
#     if num % i == 0:
#         print("\033[34m", end="")
#         qnt += 1
#     else:
#         print("\033[31m", end="")
#     print("{} ".format(i), end="")
# if qnt == 2:
#     print("\n\033[m{} é primo".format(num))
# else:
#     print("\n\033[m{} não é primo, pois é divisível {} vezes".format(num, qnt))

# exercicio 053

# os.system("cls")
# frase = str(input("Digite uma frase: ")).strip().lower()
# palavras = frase.split()
# junto = "".join(palavras)
# inverso = ""

# for letra in range(len(junto) -1, -1, -1):
#     inverso += junto[letra]
# if junto == inverso:
#     print("Temos um palíndromo")
# else:
#     print("Não temos um palíndromo")
#                   OU
# frase = input("Qual a frase? ").upper().replace(" ", "")
# if frase == frase[::-1]:
#     print("A frase é um palíndromo")
# else:
#     print("A frase não é um palíndromo")
# exercicio 054

# os.system("cls")
# contMaior = 0
# contMenor = 0
# for i in range (1, 8):
#     anoNasc = int(input("Em que ano a {}° pessoa nasceu? ".format(i)))
#     anoAtual = datetime.date.today().year
#     idade = anoAtual - anoNasc
#     if idade >= 18:
#         contMaior += 1
#     else:
#         contMenor += 1
# print("Há {} pessoas maiores de idade\nE {} pessoas menores de idade".format(contMaior, contMenor))

# exercicio 055

# os.system("cls")
# for i in range(1, 6):
#     peso = float(input("Iforme o peso (Kg) da {}° pessoa: ".format(i)))
#     if i == 1:
#         maior = peso
#         menor = peso
#     else:
#         if maior < peso:
#             maior = peso
#         if menor > peso:
#             menor = peso
# print("O maior peso lido foi de {}Kg \nE o menor peso lido foi de {}Kg".format(maior, menor))

# exercicio 056

# os.system("cls")
# cont = 0
# maior = 0
# contIdade = 0
# somaIdade = 0

# for i in range(1, 5):
#     print("----{}ª PESSOA-----".format(i))
#     nome = str(input("Nome: ")).strip()
#     idade = int(input("Idade: "))
#     sexo = str(input("Sexo [M/F]: ")).strip().lower()
#     print("")
#     somaIdade += idade
#     if sexo == "m":
#         cont += 1
#         if cont == 1:
#             maior = idade
#             nomeMais = nome
#         else:
#             if maior < idade:
#                 maior = idade
#                 nomeMais = nome
#     else:
#         if idade < 20:
#             contIdade += 1
# media = float(somaIdade/4)
# print("A média de idade do grupo é de {:.1f} anos".format(media))
# print("O homem mais velho tem {} anos e se chama {}".format(maior, nomeMais))
# print("Ao todo são {} mulheres com menos de 20 anos".format(contIdade))

#                               LAÇO WHILE

# exercicio 057
# sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()[0] # pega só a primeira letra
# while sexo != "M" and sexo != "F":
#     sexo = str(input("Sexo inválido, digite novamente [M/F]: ")).strip().upper()[0]
# print("fim")

# exercicio 058
# tentativa = 0
# numeroSorteado = random.randint(0, 10)
# print(numeroSorteado)
# palpite = -1
# print("O computador sorteou um numero entre 0 e 10, consegue adivinhar?\n")
# while palpite != numeroSorteado:
#     palpite = int(input("Digite seu palpite: "))
#     if palpite == numeroSorteado:
#         print("Parabéns!")
#     else:
#         if palpite > numeroSorteado:
#             print("O papalpite foi maior que o número sorteado...")
#         else: 
#             print("O papalpite foi menor que o número sorteado...")
#     tentativa += 1
# print("Você acertou na {}° tentativa!".format(tentativa))

#                                                   OU
# numeroSorteado = random.randint(0, 10)
# acertou = False
# tentativa = 0
# while not acertou:
#     papalpite = int(input("Digite seu palpite: "))
#     tentativa += 1
#     if papalpite == numeroSorteado:
#         acertou = True
#     else:
#         if papalpite < numeroSorteado:
#             print("O seu paplpite foi menor que o numero sorteado, tente novamente.")
#         else: 
#             print("O seu paplpite foi maior que o numero sorteado, tente novamente.")
# print("Você acertou na {}° tentativa!".format(tentativa))


# exercicio 059
# resultado = 0
# opc = 0
# while opc != 5:
#     num = int(input("\nDigite um valor: "))
#     num2 = int(input("Digite outro valor: "))
#     print("ESCOLHA")
#     print("[1] somar")
#     print("[2] multiplicar")
#     print("[3] maior")
#     print("[4] novos valores")
#     print("[5] sair do programa")
#     opc = int(input("Qual sua opção? "))
#     if opc == 1:
#         resultado = num + num2
#         print("A soma de {} e {} é {}".format(num, num2, resultado))
#     elif opc == 2:
#         resultado = num * num2
#         print("A multiplicação de {} e {} é {}".format(num, num2, resultado))
#     elif opc == 3:
#         if num > num2:
#             print("Entre {} e {} o {} é maior".format(num, num2, num))
#         elif num < num2:
#             print("Entre {} e {} o {} é maior".format(num, num2, num))
#         else:
#             print("Os valores são iguais")
#     elif opc == 4:
#         os.system("cls")
#         print("Informe os valores novamente: ")
#         num = int(input("Digite um valor: "))
#         num2 = int(input("Digite outro valor: "))
#     elif opc == 5:
#         print("Finalizando")
#     else: 
#         print("Opção inválida!")

# exercicio 060
# # com while
# fatorial = 1
# num = int(input("Digite um número para ver seu fatorial: "))
# print("Calculando {}! = ".format(num), end="")
# while num != 0:
#     print("{} ".format(num), end="")
#     print("x " if num > 1 else " = ", end="")
#     fatorial *= num
#     num -= 1
# print(fatorial)
# # com for
# fatorial = 1
# num = int(input("Digite um número para ver seu fatorial: "))
# print("Calculando {}! = ".format(num), end="")
# for i in range (num, 0, -1):
#     print("{}".format(i), end="")
#     print(" x " if i>1 else " = ", end="")
#     fatorial *= i
# print(fatorial)

# exercicio 061
# print("\033[33m="*20)
# print("\033[32m10 TERMOS DE UMA PA")
# print("\033[33m="*20,"\n")
# print("\033[m")
# pTermo = int(input("Primeiro termo: "))
# razao = int(input("Razão: "))
# cont = 1
# while cont <= 10:
#     print(pTermo, end=" → ");
#     cont += 1
#     pTermo += razao
# print("\033[31mACABOU")
# print("\033[m")

# exercicio 062
# soma = 0
# maisTermos = -1
# print("\033[33m="*20)
# print("\033[32m10 TERMOS DE UMA PA")
# print("\033[33m="*20,"\n")
# print("\033[m")
# pTermo = int(input("Primeiro termo: "))
# razao = int(input("Razão: "))
# cont = 1
# while cont <= 10:
#     print(pTermo, end=" → ");
#     cont += 1
#     pTermo += razao
# print("\033[31mPAUSA")
# print("\033[m")
# while maisTermos != 0:
#     maisTermos = int(input("\nQuantos termos você quer mostrar a mais? "))
#     soma = maisTermos + cont
#     while cont < soma:
#         print(pTermo, end=" → ")
#         cont += 1
#         pTermo += razao
#     if maisTermos != 0:
#         print("\033[31mPAUSA")
#         print("\033[m")
#     else:
#         print("\033[31mFIM")
#         print("\033[m")
#                                         OU
# print("\033[33m="*20)
# print("\033[32m10 TERMOS DE UMA PA")
# print("\033[33m="*20,"\n")
# print("\033[m")
# pTermo = int(input("Primeiro termo: "))
# razao = int(input("Razão: "))
# cont = 1
# total = 0
# maisTermos = 10
# while maisTermos != 0:
#     total += maisTermos
#     while cont <= total:
#         print(pTermo, end=" → ")
#         pTermo += razao
#         cont += 1
#     print("\033[31mPAUSA")
#     print("\033[m")
#     maisTermos = int(input("\nQuantos termos você quer mostrar a mais? "))
# print("\033[31mFIM")
# print("\033[m")

# exercicio 063
# print("Sequência de Fibonacci")
# num = int(input("Quantos termos você quer mostrar? "))
# t1 = 0
# t2 = 1
# if num == 1:
#     print("{}".format(t1, t2), end="")
#     print("\033[31m → FIM")
# elif num == 0 or num < 0:
#     print("Número inválido!")
# else:
#     print("{} → {}".format(t1, t2), end="")
#     cont = 3
#     while cont <= num:
#         t3 = t1 + t2
#         print(" → {}".format(t3), end="")
#         t1 = t2
#         t2 = t3
#         cont += 1
#     print("\033[31m → FIM")
# print("\033[m")

# exercicio 064
# cont = 1
# soma = 0
# num = 0
# while num != 999:
#     num = int(input("Digite um valor [999 para parar]: "))
#     if num != 999:
#         soma += num
#         cont += 1
# print("Foram digitado ao todo {} números, e a soma deles foi {}".format(cont, soma))

# exercicio 065
# num = 0
# r = "S"
# cont = 0
# soma = 0
# maior = 0
# menor = 0
# while r == "S":
#     num = int(input("Digite um valor: "))
#     if cont == 1:
#         maior = menor = num
#     if num > maior:
#         maior = num
#     if num < menor:
#         menor = num
#     r = str(input("Deseja continuar [S/N]? ")).strip().upper()
#     soma += num
#     cont += 1
# media = soma/cont
# print("A média dos valores digitados foi de {}, o maior número digitado foi o {} e o menor foi o {}".format(media, maior, menor))

#                               WHILE COM BREAK

# exercicio 066
# soma = 0
# while True:
#     num = int(input("Digite um valor [999 para parar]: "))
#     if num == 999:
#         print(f"A soma dos valores digitados foi {soma}")
#         break
#     soma += num

# exercicio 067
# while True:
#     num = int(input("Digite um valor para ver a tabuada: "))
#     if num < 0:
#         print("Até a próxima!")
#     break
#     for i in range(1, 11):
#         print(f"{i} x {num} = {num*i}")

# exercicio 068
# cont = 0
# while True:
#     comp = random.randint(1, 10)
#     esc = " "
#     print("PAR OU ÍMPAR COM O COMPUTADOR")
#     print("-=-"*20)
#     jog = int(input("Digite um valor: "))
#     total = jog + comp
#     resul = total % 2
#     while esc not in "PI":
#         esc = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
#     if esc == "P":
#         if resul == 0:
#             print(f"Você ganhou :), o computador jogou {comp} você jogou {jog} e o total foi {total}, DEU PAR")
#             print("Jogue novamente")
#             cont += 1
#         else:
#             print(f"Você perdeu :( o computador jogou {comp} você jogou {jog} e o total foi {total}, DEU ÍMPAR")
#             break
#     elif esc == "I":
#         if resul == 1:
#             print(f"Você ganhou :), o computador jogou {comp} você jogou {jog} e o total foi {total}, DEU ÍMPAR")
#             print("Jogue novamente")
#             cont += 1
#         else:
#             print(f"Você perdeu :(, o computador jogou {comp} você jogou {jog} e o total foi {total}, DEU PAR")
#             break
#     else:
#         print("Opção inválida!")
# print(f"GAME OVER! Você venceu {cont} vezes")

# exercicio 069
# mais = 0
# homens = 0
# menos = 0
# while True:
#     sexo = " "
#     escolha = " "
#     print("="*20)
#     print("CADASTRE UMA PESSOA")
#     print("="*20)
#     idade = int(input("Idade: "))
#     if idade >= 18:
#         mais += 1
#     while sexo not in "MF":
#         sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
#     if sexo == "M":
#         homens += 1
#     if sexo == "F" and idade < 20:
#         menos += 1
#     while escolha not in "SN":
#         escolha = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
#     if escolha == "N":
#         print("Imprimindo análises...")
#         break
# print(f"Total de pessoas com mais de 18 anos: {mais}")
# print(f"Ao todo temos {homens} homens cadastrados")
# print(f"E temos {menos} mulheres com menos de 20 anos")

# exercicio 070
# mBarato = total = cont = mMil = 0
# nomeBarato = " "
# while True:
#     nome = str(input("Nome do produto: "))
#     valor = float(input("Preço: R$"))
#     total += valor
#     cont += 1
#     if cont == 1:
#         mBarato = valor
#         nomeBarato = nome
#     else:
#         if valor < mBarato:
#             mBarato = valor
#             nomeBarato = nome
#     if valor > 1000:
#         mMil += 1
#     continua = " "
#     while continua not in "sn":
#         continua = str(input("Quer continuar? [S/N] ")).strip().lower()[0]
#     if continua == "n":
#         break
# print(f"Total gasto na compra é de: R${total}")
# print(f"Os produtos que custam mais de R$1000,00 são: {mMil}")
# print(f"O nome do produto mais barato é: {nomeBarato}")

# exercicio 071
# valor = int(input("Digite o valor a ser sacado: R$"))
# total = valor
# cedula = 50
# qntCedula = 0
# while True:
#     if total >= cedula:
#         total -= cedula
#         qntCedula += 1
#     else:
#         if qntCedula > 0:
#             print(f"Total de {qntCedula} cédulas de R${cedula}")
#         if cedula == 50:
#             cedula = 20
#         elif cedula == 20:
#             cedula = 10
#         elif cedula == 10:
#             cedula = 1
#         qntCedula = 0
#         if total == 0:
#             break
# #                         FORMA MEGA OTIMIZADA
# valorSaque = int(input('Valor do saque: R$ '))
# print('-' * 40)
# for nota in [50, 20, 10, 1]:
#     quantidade = valorSaque // nota
#     valorSaque = valorSaque % nota
#     if quantidade > 0:
#         print(f'{quantidade} notas de R$ {nota}')
# #                         FORMA MAIS MATEMÁTICA
# valor = int(input("Digite o valor a ser sacado: R$"))
# nota50 = valor // 50
# valor %=  50
# nota20 = valor // 20
# valor %= 20
# nota10 = valor // 10
# valor %= 10
# nota1 = valor // 1
# print(f"notas de 50 = {nota50}")
# print(f"notas de 20 = {nota20}")
# print(f"notas de 10 = {nota10}")
# print(f"notas de 1 = {nota1}")

