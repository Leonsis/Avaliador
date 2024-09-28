from flask import Flask, request, jsonify, render_template, send_from_directory
import json
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

# Carregar gabarito do arquivo JSON
def load_gabarito():
    with open('gabarito.json', 'r') as file:
        return json.load(file)

# Função para salvar o gabarito no arquivo JSON
def save_gabarito(gabarito):
    with open('gabarito.json', 'w') as file:
        json.dump(gabarito, file, indent=4)

# Função para comparar respostas do usuário com o gabarito
def corrigir_respostas(respostas_usuario, gabarito):
    pontuacao = 0
    for questao, resposta in respostas_usuario.items():
        if questao in gabarito and resposta == gabarito[questao]:
            pontuacao += 1
    return pontuacao

# Rota principal para servir o arquivo index.html na raiz
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Rota para carregar o gabarito para edição
@app.route('/gabarito', methods=['GET'])
def get_gabarito():
    gabarito = load_gabarito()
    return jsonify(gabarito)

# Rota para atualizar o gabarito
@app.route('/gabarito', methods=['POST'])
def update_gabarito():
    novos_dados = request.json
    save_gabarito(novos_dados)
    return jsonify({"status": "Gabarito atualizado com sucesso!"})

# Rota para servir arquivos estáticos (JS e CSS)
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
