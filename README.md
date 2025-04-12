# Avaliador

O **Avaliador** é uma aplicação web que permite comparar respostas de alunos com um gabarito pré-definido, facilitando a correção automatizada de provas ou exercícios.

## Funcionalidades

- Interface web para envio de respostas.
- Comparação automática com o gabarito.
- Exibição de resultados e feedback imediato.

## Tecnologias Utilizadas

- Python (Flask)
- HTML, CSS e JavaScript
- JSON para armazenamento do gabarito

## Estrutura do Projeto

- `app.py`: Arquivo principal que inicia o servidor Flask e define as rotas da aplicação.
- `gabarito.json`: Contém as respostas corretas para comparação.
- `index.html`: Página principal da aplicação onde os usuários podem enviar suas respostas.
- `static/`: Pasta que contém arquivos estáticos como CSS e JavaScript.
- `requirements.txt`: Lista de dependências necessárias para executar o projeto.
- `Procfile`: Arquivo de configuração para implantação em plataformas como Heroku.

## Como Executar Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/Leonsis/Avaliador.git
   cd Avaliador

2. Crie um ambiente virtual e ative-o:

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate


3. Instale as dependências:

pip install -r requirements.txt


4. Inicie a aplicação:

python app.py


5. Acesse http://localhost:5000 no seu navegador para utilizar a aplicação.



Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias.

Licença

Este projeto está licenciado sob a MIT License.
