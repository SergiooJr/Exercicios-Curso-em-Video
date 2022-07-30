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
num = leiaInt("Digite um valor: ")
print(f"O valor digitado foi {num}")