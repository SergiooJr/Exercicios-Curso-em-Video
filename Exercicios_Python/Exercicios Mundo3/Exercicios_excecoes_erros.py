# exercicio 113
def leiaInt(v):
    while True:
        try:
            n = int(input(v))
        except (TypeError, ValueError):
            print("\033[31mERRO! Por favor digite um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("Entrada de dados interrompida pelo usuário!")
        else:
            return n

def leiaFloat(v):
    while True:
        try:
            num = float(input(v))
        except (TypeError, ValueError):
            print("\033[31mERRO! Por favor digite um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("Entrada de dados interrompida pelo usuário!")
        else:
            return num

num = leiaInt("Digite um valor inteiro: ")
numF = leiaFloat("Digite um valor real: ")
print(f"O valor inteiro digitado foi {num}, e o real foi {numF}")