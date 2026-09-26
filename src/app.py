import pandas as pd
import json
import streamlit as st
from ollama import chat

#Aparecencia
st.set_page_config(
    page_title="DengueBot",
    page_icon="🦟",
    layout="centered"
)

## Carregar dados

aedes = json.load(open('./data/aedes_aegypti.json', encoding='utf-8'))
historico = pd.read_csv('./data/historico_atendimento.csv', encoding='utf-8')
prevencao = json.load(open('./data/prevencao.json', encoding='utf-8'))
sintomas = json.load(open('./data/sintomas.json', encoding='utf-8'))


## Verificar dados carregados

print("Aedes:", len(aedes))
print("Histórico:", len(historico))
print("Prevenção:", len(prevencao["medidas"]))
print("Sintomas:", len(sintomas))

## Montar contexto da base de conhecimento


def montar_contexto():
    sintomas_comuns = [
        item for item in sintomas
        if item["categoria"] == "sintoma_comum"
    ]

    sinais_alerta = [
        item for item in sintomas
        if item["categoria"] == "sinal_de_alerta"
    ]

    contexto = f"""
PREVENÇÃO DA DENGUE:
{prevencao}

AEDES AEGYPTI:
{aedes}

SINTOMAS COMUNS DA DENGUE:
{sintomas_comuns}

SINAIS DE ALERTA DA DENGUE:
{sinais_alerta}
"""
    return contexto


contexto = montar_contexto()

print("\n--- CONTEXTO ---")
print(contexto)

## Responder perguntas simples
## Responder perguntas usando o Ollama

def responder(pergunta):
    pergunta_lower = pergunta.lower()

    if any(palavra in pergunta_lower for palavra in [
        "remédio",
        "remedio",
        "medicamento",
        "medicamentos",
        "o que tomar",
        "posso tomar",
        "qual remédio",
        "qual remedio",
        "que remédio",
        "que remedio",
        "tomar para",
        "usar para",
        "uso de medicamento",
         "estou com dengue",
        "tenho dengue",
        "acho que estou com dengue",
        "estou com sintomas",
        "tenho sintomas",
        "estou com febre",
        "estou com dor",
        "tenho dor",
        "estou piorando",
        "não estou melhorando",
        "nao estou melhorando",
        "o que faço se",
        "como tratar",
        "tratamento"
    ]):
       return "Não encontrei essa informação na minha base de conhecimento. Não consigo te ajudar com isso. Procure um profissional de saúde."
    
    contexto = montar_contexto()

    if "sintomas comuns" in pergunta_lower:
        sintomas_comuns = [
            item for item in sintomas
            if item["categoria"] == "sintoma_comum"
        ]

        contexto = f"""
SINTOMAS COMUNS DA DENGUE:
{sintomas_comuns}
"""

    elif "sinais de alerta" in pergunta_lower or "sinais de alarme" in pergunta_lower:
        sinais_alerta = [
            item for item in sintomas
            if item["categoria"] == "sinal_de_alerta"
        ]

        contexto = f"""
SINAIS DE ALERTA DA DENGUE:
{sinais_alerta}
"""

    resposta = chat(
        model='qwen2.5:3b',
        messages=[
            {
                'role': 'system',
                'content': f"""
Você é o DengueBot, um assistente virtual educativo sobre dengue.

Responda utilizando somente as informações disponíveis na base de conhecimento fornecida nesta mensagem.

JAMAIS responda perguntas fora do tema da dengue.

Não invente informações.
Não utilize conhecimento externo.
Não adicione fatos que não estejam na base de conhecimento.
Não altere o significado das informações da base.

Você pode organizar e explicar as informações de forma natural, mas deve permanecer fiel ao conteúdo fornecido.

Se a pergunta não puder ser respondida com as informações disponíveis, diga:
"Não encontrei essa informação na minha base de conhecimento."

Você não realiza diagnósticos, não prescreve medicamentos e não define tratamentos.

BASE DE CONHECIMENTO:
{contexto}
"""
            },
            {
                'role': 'user',
                'content': pergunta
            }
        ],
    )

    return resposta.message.content

#Estilo pagina web
st.markdown("""
<div style="
    background-color: #e8f5e9;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 25px;
">
    <h1 style="margin-bottom: 8px;">🦟 DengueBot</h1>
    <p style="font-size: 18px; margin: 0;">
        Assistente virtual educativo sobre dengue e prevenção!
    </p>
    <p style="font-size: 18px; margin: 0;">
            Olá! Eu sou o DengueBot. Como posso te ajudar hoje?
    </p>
</div>
""", unsafe_allow_html=True)


if "mensagens" not in st.session_state:
    st.session_state.mensagens = []


for mensagem in st.session_state.mensagens:
    st.chat_message(mensagem["role"]).write(mensagem["content"])


pergunta = st.chat_input("Digite sua pergunta sobre dengue...")

if pergunta:
    st.session_state.mensagens.append({
        "role": "user",
        "content": pergunta
    })

    st.chat_message("user").write(pergunta)

    resposta = responder(pergunta)

    st.session_state.mensagens.append({
        "role": "assistant",
        "content": resposta
    })

    st.chat_message("assistant").write(resposta)