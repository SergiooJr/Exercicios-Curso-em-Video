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