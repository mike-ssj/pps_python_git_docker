from frases_mongo import consultar, add

def frotar(n_frases: int = 1) -> list:
    return consultar(n_frases)

def add_frases(lista_frases: list):
    add(lista_frases)
