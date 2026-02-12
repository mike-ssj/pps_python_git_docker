from pymongo import MongoClient

datos = [
    {"frase": "El éxito es como un fantasma, muchos hablan de él, pero pocos lo han visto de verdad"},
    {"frase": "La aventura de hoy es la historia de terror del mañana"},
    {"frase": "La felicidad es como un rayo de sol, disfrútala antes de que el cambio climático la arruine"},
    {"frase": "Enfrenta tus miedos, o pídeles alquiler por vivir en tu cabeza"},
    {"frase": "Recuerda, cada pequeño cambio cuenta. Especialmente los errores en tu declaración de la renta"},
    {"frase": "Aprovecha las oportunidades, son como los autobuses, los que no llegan tarde simplemente no pasan"},
    {"frase": "Ser agradecido está bien, pero no paga las facturas"},
    {"frase": "La creatividad es como jugar a la ruleta rusa, nunca sabes cuándo te tocará una 'buena' idea"},
    {"frase": "Ríe y el mundo reirá contigo. Llora, y te darán una cuenta de Twitter"},
    {"frase": "Sigue tu corazón, pero recuerda llevar tu cerebro contigo"}
]

def instanciar():
    cliente_mongo = MongoClient('mongodb://mongodb:27017/')
    bd = cliente_mongo['bayeta'] 
    frases_auspiciosas = bd['frases_auspiciosas'] 
    return cliente_mongo, frases_auspiciosas

def add(frases: list):
    cliente_mongo, frases_auspiciosas = instanciar()

    if frases_auspiciosas.count_documents({}) == 0:
        frases_auspiciosas.insert_many(frases)
    cliente_mongo.close()


def consultar(n_frases: int):
    cliente_mongo, frases_auspiciosas = instanciar()
    frases_aleatorias = list(frases_auspiciosas.aggregate([{"$sample": {"size": n_frases}}]))
    cliente_mongo.close()
    return [f["frase"] for f in frases_aleatorias]


def inicializar():
    cliente_mongo, frases_auspiciosas = instanciar()
    
    if frases_auspiciosas.count_documents({}) == 0:
        with open("frases.txt", "r") as f:
            frases = []
            for linea in f:
                frases.append({"frase": linea.strip()})
        frases_auspiciosas.insert_many(frases)
    
    cliente_mongo.close()
    

if __name__ == "__main__":
    inicializar()
