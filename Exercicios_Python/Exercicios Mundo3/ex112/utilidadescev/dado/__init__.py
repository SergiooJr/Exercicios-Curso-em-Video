
def leiaDinheiro(n):
    while True:
        num = str(input(n)).replace(",", ".")
        if num.isalpha() or num.strip() == "":
            print(f"\033[0;31mERRO! \"{num}\" é um preço inválido.\033[m")
        else:
            return float(num)