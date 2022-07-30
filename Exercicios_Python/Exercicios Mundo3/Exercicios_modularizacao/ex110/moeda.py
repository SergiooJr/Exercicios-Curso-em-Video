def metade(n=0,formata=False):
    if formata:
        return moeda(n/2)
    else:
        return n/2

def dobro(n=0, formata=False):
    if formata:
        return moeda(n*2)
    else:
        return n*2

def aumentar(n=0, p=0, formata=False):
     return moeda(n+(n*p/100)) if formata is True else n+(n*p/100)

def diminuir(n=0, p=0, formata=False):
    if formata: 
        return moeda(n-(n*p/100))
    else: 
        return n-(n*p/100)

def moeda(n=0, moeda="R$"):
    return f"{moeda}{n:.2f}".replace(".", ",")

def resumo(n=0, amt=0, dmn=0):
    print("-"*30)
    print("RESUMO DO VALOR".center(30))
    print("-"*30)
    print(f"Preço analisado: \t{moeda(n)}.")
    print(f"A metade do preço: \t{metade(n, True)}.")
    print(f"O dobro do preço: \t{dobro(n, True)}.")
    print(f"Aumentando {amt}% temos: \t{aumentar(n, amt, True)}.")
    print(f"Diminuindo {dmn}% temos: \t{diminuir(n, dmn, True)}.")
    print("-"*30)