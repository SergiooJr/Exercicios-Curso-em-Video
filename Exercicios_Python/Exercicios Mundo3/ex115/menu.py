from time import sleep

def l():
    print("-"*30)
def leiaInt(v):
    while True:
        n = input(v)
        if n.isalpha():
            print("Digite um número inteiro válido!")
            continue
        else:
            return int(n)

def verPessoasCad():
    try:
        with open(r"C:\Users\jessi\OneDrive\Documentos\GitHub\Exercic-os-Curso-em-V-deo\Exercicios_Python\Exercicios Mundo3\ex115\pessoasCad.txt", "r") as arquivo:
            for valores in arquivo:
                print(valores)
        sleep(2)
    except FileNotFoundError:
        print("O arquivo está vázio, adicione uma pessoa!")
        sleep(2)
def CadNovPessoa():
    l()
    print("NOVO CADASTRO".center(30))
    l()
    nome = str(input("Nome: ")).strip()
    idade = leiaInt("Idade: ")
    with open(r"C:\Users\jessi\OneDrive\Documentos\GitHub\Exercic-os-Curso-em-V-deo\Exercicios_Python\Exercicios Mundo3\ex115\pessoasCad.txt", "a") as arquivo:
        arquivo.write(f"{nome} \t\t{idade} anos\n")
    print("Cadastro realizado com sucesso!")
    sleep(2)
while True:
    l()
    print("MENU PRINCIPAL".center(30))
    l()
    print("1 - Ver pessoas cadastradas")
    print("2 - Cadastrar nova pessoa")
    print("3 - Sair do sistema")
    while True:
        opc = leiaInt("Sua opção: ")
        if opc > 0 and opc < 4:
            print("Um momento...")
            sleep(1)
            break
        else:
            print("O número digitado não é uma das opções!")
    if opc == 1:
        verPessoasCad()
    elif opc == 2:
        CadNovPessoa()
    else:
        print("Até a próxima!")
        break


