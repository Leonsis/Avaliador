from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

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

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint para corrigir respostas
@app.route('/corrigir', methods=['POST'])
def corrigir():
    dados = request.json
    respostas_usuario = dados.get('respostas', {})
    gabarito = load_gabarito()
    pontuacao = corrigir_respostas(respostas_usuario, gabarito)
    return jsonify({'pontuacao': pontuacao})

# Endpoint para carregar o gabarito para edição
@app.route('/gabarito', methods=['GET'])
def get_gabarito():
    gabarito = load_gabarito()
    return jsonify(gabarito)

# Endpoint para atualizar o gabarito
@app.route('/gabarito', methods=['POST'])
def update_gabarito():
    novos_dados = request.json
    save_gabarito(novos_dados)
    return jsonify({"status": "Gabarito atualizado com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)
