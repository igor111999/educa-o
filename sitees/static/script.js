let perguntaatual = 0;
let respostacorreta = 0;


criarperguntas();

function criarperguntas() {
    if (perguntas[perguntaatual]) {
        let q = perguntas[perguntaatual];

        let pct = Math.floor((perguntaatual / perguntas.length) * 100);

        document.querySelector('.barradeprogresso').style.width = `${pct}%`;

        document.querySelector('.areadepontuacao').style.display = 'none';
        document.querySelector('.areadepergunta').style.display = 'block';

        document.querySelector('.pergunta').innerHTML = q.pergunta;
        document.querySelector('.opcoes').innerHTML = '';

        let opcoesHtml = '';
        for (let i in q.opcoes) {
            opcoesHtml += `<div data-op="${i}" class="opcao"><span>${parseInt(i)+1}</span>${q.opcoes[i]}</div>`;
        }
        document.querySelector('.opcoes').innerHTML = opcoesHtml;

        document.querySelectorAll('.opcoes .opcao').forEach(item => {
            item.addEventListener('click', opcaoClickEvent);
        });


    } else {
        finishQuiz();
    }
}

function opcaoClickEvent(e) {
    let clickedopcao = parseInt(e.target.getAttribute('data-op'));

    if (perguntas[perguntaatual].answer === clickedopcao) {
        respostacorreta++;
    }

    perguntaatual++;
    criarperguntas();
}

document.querySelector('.areadepontuacao button').addEventListener('click', resetEvent);

function finishQuiz() {
    let points = Math.floor((respostacorreta / perguntas.length) * 100);

    if (points < 30) {
        document.querySelector('.prizeImage').src = './static/imgs/Gold.png';
        document.querySelector('.venceu').innerHTML = 'Parabéns, você é fera!';
        document.querySelector('.pctdacerto').style.color = '#0D630D';
    } else if (points >= 30 && points < 70) {
        document.querySelector('.prizeImage').src = './static/imgs/Gold.png';
        document.querySelector('.venceu').innerHTML = 'Parabéns, você é fera!';
        document.querySelector('.pctdacerto').style.color = '#0D630D';
    } else if (points >= 70) {
        document.querySelector('.prizeImage').src = './static/imgs/Gold.png';
        document.querySelector('.venceu').innerHTML = 'Parabéns, você é fera!';
        document.querySelector('.pctdacerto').style.color = '#0D630D';
    }

    document.querySelector('.pctdacerto').innerHTML = 'Muito Bom!';
    document.querySelector('.qtddacerto').innerHTML = 'Você concluiu o seu estudo';

    document.querySelector('.areadepontuacao').style.display = 'block';
    document.querySelector('.areadepergunta').style.display = 'none';
    document.querySelector('.barradeprogresso').style.width = `100%`;
}

function resetEvent() {
    respostacorreta = 0;
    perguntaatual = 0;
    criarperguntas();
}