import random
from frases_mongo import consultar

def frotar(n_frases: int = 1) -> list:
    return consultar(n_frases)
