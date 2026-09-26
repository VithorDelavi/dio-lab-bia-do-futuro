# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `prevencao.json` | JSON | Fornecer informações sobre medidas de prevenção e eliminação de possíveis criadouros do Aedes aegypti |
| `sintomas.json` | JSON | Fornecer informações educativas sobre sintomas da dengue e sinais de alerta |
| `aedes_aegypti.json` | JSON | Apresentar informações sobre o mosquito Aedes aegypti, seu ciclo de vida e seus criadouros |
| `orientacoes.json` | JSON | Fornecer orientações gerais sobre cuidados e situações em que o usuário deve buscar atendimento profissional |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados foram adaptados do contexto financeiro original do projeto para o contexto de educação e prevenção da dengue. A base de conhecimento foi organizada em arquivos JSON separados por tema, contendo informações sobre prevenção, sintomas, o mosquito Aedes aegypti e orientações gerais de saúde.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos JSON da pasta `data/` são carregados pela aplicação quando o DengueBot é iniciado. As informações desses arquivos são organizadas e disponibilizadas como contexto para o agente durante as interações com o usuário.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

As informações da base de conhecimento são inseridas no contexto enviado ao modelo de linguagem junto às instruções do DengueBot. O agente deve utilizar essas informações para responder às perguntas do usuário, sem inventar dados que não estejam disponíveis na base. Quando a informação solicitada não estiver presente, o agente deve informar que não possui dados suficientes para responder.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

Tema: Prevenção da dengue

Informações disponíveis:
- Medidas de prevenção contra a dengue
- Identificação de possíveis criadouros do Aedes aegypti
- Informações sobre sintomas da dengue
- Informações sobre o ciclo de vida do Aedes aegypti
- Orientações gerais e situações em que o usuário deve buscar atendimento profissional

Regra de resposta:
Utilize somente as informações disponíveis na base de conhecimento. Caso a informação solicitada não esteja disponível, informe ao usuário que não possui dados suficientes para responder e não invente uma resposta.
