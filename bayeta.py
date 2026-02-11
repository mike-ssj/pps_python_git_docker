import random

def frotar(n_frases: int = 1) -> list:
    try:
        with open('frases.txt', 'r', encoding='utf-8') as f:
            todas_las_frases = [linea.strip() for linea in f if linea.strip()]
        
        if not todas_las_frases:
            return ["No hay frases disponibles en este momento."]
            
        frases_elegidas = random.choices(todas_las_frases, k=n_frases)
        
        return frases_elegidas

    except FileNotFoundError:
        return ["Error: El archivo frases.txt no existe."]