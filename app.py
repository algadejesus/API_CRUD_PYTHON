from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'Bíblia Sagrada - Nova Versão Internacional - NVI',
        'autor': 'Deus Todo-poderoso'
    },
    {
        'id': 2,
        'título': 'Harry potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'título': 'James Clear',
        'autor': 'Hábitos Atômicos'
    },
    {
        'id': 4,
        'título': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    }
]

@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>' ,methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

@app.route('/livros/<int:id>' ,methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

@app.route('/livros' ,methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

@app.route('/livros/<ind:id>' ,methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)