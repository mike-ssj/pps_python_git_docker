print("Hello World")

from bayeta import frotar, add_frases
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "<h1>Hello World</h1>"


@app.route('/frotar/<int:n_frases>')
def api_frotar(n_frases):
    frases = frotar(n_frases)
    return jsonify({"frases": frases, "cantidad": n_frases})

@app.route('/frotar/add', methods=['POST'])
def api_add_frases():
    data = request.get_json() 

    if not isinstance(data, list) or not all(isinstance(f, dict) and "frase" in f for f in data):
        return jsonify({"error": 'Espera [{"frase": "..."}]'}), 400
    
    add_frases(data)
    
    return jsonify({"output": f"Se han añadido {len(data)} frases"}), 200


def main():
    app.run(debug=True, host="0.0.0.0", port=5000)
    # print(f"Resultado de frotar: {frotar(1)}")

if __name__ == "__main__":
    main()