print("Hello World")

from bayeta import frotar
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "<h1>Hello World</h1>"


@app.route('/frotar/<int:n_frases>')
def api_frotar(n_frases):
    frases = frotar(n_frases)
    return jsonify({"frases": frases, "cantidad": n_frases})


def main():
    app.run(debug=True, port=5000)
    # print(f"Resultado de frotar: {frotar(1)}")

if __name__ == "__main__":
    main()