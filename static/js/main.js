// Função para gerar dinamicamente as questões
function gerarQuestoes() {
    const numQuestoes = document.getElementById('numeroQuestoes').value;
    document.getElementById('numQuestoesDisplay').innerText = numQuestoes;

    const form = document.getElementById('form-gabarito');
    form.innerHTML = '';  // Limpa o formulário

    for (let i = 1; i <= numQuestoes; i++) {
        const div = document.createElement('div');
        div.classList.add('questao');
        div.innerHTML = `
            <label for="questao${i}">Questão ${i}:</label>
            <input type="text" id="questao${i}" name="questao${i}" placeholder="Resposta da questão ${i}">
        `;
        form.appendChild(div);
    }
}

// Atualiza as questões quando o slider for alterado
gerarQuestoes();

// Função para corrigir as respostas
function corrigirGabarito() {
    const numQuestoes = document.getElementById('numeroQuestoes').value;
    const respostas = {};

    for (let i = 1; i <= numQuestoes; i++) {
        respostas[i] = document.getElementById(`questao${i}`).value;
    }

    fetch('/corrigir', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ respostas })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('resultado').innerHTML = `Sua pontuação: ${data.pontuacao}/${numQuestoes}`;
    });
}

// Função para carregar o gabarito atual e exibi-lo para edição
function carregarGabarito() {
    fetch('/gabarito', {
        method: 'GET'
    })
    .then(response => response.json())
    .then(gabarito => {
        const formEdit = document.getElementById('edit-gabarito-form');
        formEdit.innerHTML = '';  // Limpa o formulário

        for (const questao in gabarito) {
            const div = document.createElement('div');
            div.classList.add('questao');
            div.innerHTML = `
                <label for="edit-questao${questao}">Questão ${questao}:</label>
                <input type="text" id="edit-questao${questao}" value="${gabarito[questao]}" placeholder="Resposta da questão ${questao}">
            `;
            formEdit.appendChild(div);
        }
    });
}

// Função para salvar o gabarito alterado
function salvarGabarito() {
    const formEdit = document.getElementById('edit-gabarito-form');
    const inputs = formEdit.querySelectorAll('input');
    const gabaritoAtualizado = {};

    inputs.forEach(input => {
        const questao = input.id.replace('edit-questao', '');
        gabaritoAtualizado[questao] = input.value;
    });

    fetch('/gabarito', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(gabaritoAtualizado)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.status);
    });
}

// Carrega o gabarito atual ao iniciar a página
carregarGabarito();
