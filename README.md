# 🦟 DengueBot — Assistente Virtual Educativo com IA

## Contexto

Os assistentes virtuais com Inteligência Artificial podem ser utilizados para facilitar o acesso a informações de diferentes áreas. Neste desafio, a proposta original é idealizar e prototipar um agente inteligente utilizando IA Generativa, uma base de conhecimento e mecanismos de segurança.

Neste projeto, a ideia foi adaptada para o contexto de **educação em saúde**, criando o **DengueBot**, um assistente virtual educativo sobre dengue.

O DengueBot utiliza IA Generativa para:

- **Responder dúvidas** sobre dengue, prevenção e o mosquito Aedes aegypti;
- **Utilizar uma base de conhecimento** organizada para orientar suas respostas;
- **Apresentar informações de forma simples e clara**;
- **Evitar informações inventadas** sempre que possível;
- **Informar quando não possui determinada informação**;
- **Manter limites de segurança**, evitando diagnósticos, prescrições de medicamentos e orientações de tratamento.

> [!TIP]
> Na pasta [`examples/`](./examples/) você encontra referências de implementação para cada etapa deste desafio.

---

## O Que Você Deve Entregar

### 1. Documentação do Agente

Defina **o que** seu agente faz e **como** ele funciona:

- **Caso de Uso:** Qual problema o agente resolve? O DengueBot foi desenvolvido para facilitar o acesso a informações educativas sobre dengue e prevenção.
- **Persona e Tom de Voz:** Como o agente se comporta e se comunica?
- **Arquitetura:** Fluxo de dados e integração com a base de conhecimento.
- **Segurança:** Como evitar alucinações e garantir respostas confiáveis?

📄 **Documentação do projeto:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

A base de conhecimento do DengueBot está organizada na pasta [`data/`](./data/):

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `aedes_aegypti.json` | JSON | Informações sobre o Aedes aegypti, ciclo de vida, criadouros e prevenção |
| `historico_atendimento.csv` | CSV | Histórico fictício de atendimentos relacionados ao tema |
| `prevencao.json` | JSON | Medidas de prevenção da dengue |
| `sintomas.json` | JSON | Sintomas comuns e sinais de alerta da dengue |

Os dados foram adaptados ao contexto do projeto para fornecer informações específicas ao DengueBot.

📄 **Documentação da base:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

Documente os prompts que definem o comportamento do seu agente:

- **System Prompt:** Instruções gerais de comportamento e restrições;
- **Exemplos de Interação:** Cenários de uso com entrada e saída esperada;
- **Tratamento de Edge Cases:** Como o agente lida com situações limite, informações inexistentes e perguntas fora do escopo.

O prompt do DengueBot estabelece que o agente deve utilizar as informações disponíveis na base de conhecimento, evitar inventar informações e informar suas limitações quando necessário.

📄 **Documentação dos prompts:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

Foi desenvolvido um **protótipo funcional** do DengueBot utilizando:

- Chatbot interativo desenvolvido com **Streamlit**;
- Integração com um modelo de linguagem local;
- Modelo **Qwen2.5 3B** executado através do **Ollama**;
- Conexão com a base de conhecimento em arquivos JSON e CSV;
- Validações para situações relacionadas a medicamentos e tratamento.

📁 **Código da aplicação:** [`src/app.py`](./src/app.py)

---

### 5. Avaliação e Métricas

A qualidade do DengueBot foi avaliada por meio de testes estruturados envolvendo diferentes tipos de perguntas.

Foram avaliados aspectos como:

- **Assertividade** das respostas;
- **Segurança** e prevenção de informações inventadas;
- **Coerência** com o papel definido para o agente;
- Comportamento diante de informações inexistentes;
- Comportamento diante de perguntas fora do escopo;
- Comportamento diante de perguntas relacionadas a medicamentos e tratamento.

📄 **Avaliação e métricas:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

O projeto também possui um roteiro de **pitch de 3 minutos**, apresentando:

- Qual problema o DengueBot busca resolver;
- Como a solução funciona;
- Como a Inteligência Artificial é utilizada;
- Como a base de conhecimento contribui para as respostas;
- Quais são os mecanismos de segurança;
- Quais possibilidades de evolução existem para o projeto.

📄 **Roteiro do pitch:** [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## Ferramentas Sugeridas

O desafio permite utilizar diferentes ferramentas para desenvolver o agente.

Neste projeto, foram utilizadas principalmente:

| Categoria | Ferramentas |
|-----------|-------------|
| **LLM** | [Ollama](https://ollama.ai/) + Qwen2.5 3B |
| **Desenvolvimento** | [Python](https://www.python.org/) + [Streamlit](https://streamlit.io/) |
| **Versionamento** | [Git](https://git-scm.com/) + [GitHub](https://github.com/) |
| **Diagramas** | [Mermaid](https://mermaid.js.org/) |

Outras ferramentas sugeridas originalmente pelo desafio também podem ser utilizadas:

| Categoria | Ferramentas |
|-----------|-------------|
| **LLMs** | [ChatGPT](https://chat.openai.com/), [Copilot](https://copilot.microsoft.com/), [Gemini](https://gemini.google.com/), [Claude](https://claude.ai/), [Ollama](https://ollama.ai/) |
| **Desenvolvimento** | [Streamlit](https://streamlit.io/), [Gradio](https://www.gradio.app/), [Google Colab](https://colab.research.google.com/) |
| **Orquestração** | [LangChain](https://www.langchain.com/), [LangFlow](https://www.langflow.org/), [CrewAI](https://www.crewai.com/) |
| **Diagramas** | [Mermaid](https://mermaid.js.org/), [Draw.io](https://app.diagrams.net/), [Excalidraw](https://excalidraw.com/) |

---

## Estrutura do Repositório

```text
📁 dio-lab-bia-do-futuro/
│
├── 📄 README.md
│
├── 📁 data/                              # Base de conhecimento
│   ├── aedes_aegypti.json                 # Informações sobre o Aedes aegypti
│   ├── historico_atendimento.csv          # Histórico fictício de atendimentos
│   ├── prevencao.json                     # Medidas de prevenção
│   └── sintomas.json                      # Sintomas e sinais de alerta
│
├── 📁 docs/                              # Documentação do projeto
│   ├── 01-documentacao-agente.md          # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md            # Estratégia da base de conhecimento
│   ├── 03-prompts.md                      # Prompts e comportamento do agente
│   ├── 04-metricas.md                     # Avaliação e métricas
│   └── 05-pitch.md                        # Roteiro do pitch
│
├── 📁 src/                               # Código da aplicação
│   └── app.py                             # Aplicação Streamlit
│
├── 📁 assets/                            # Imagens e outros recursos
│
└── 📁 examples/                          # Referências e exemplos
    └── README.md
```

---

## Dicas Finais

1. **Comece pelo prompt:** Um bom system prompt ajuda a definir o comportamento e os limites do agente.
2. **Organize a base de conhecimento:** Informações estruturadas ajudam o agente a responder de forma mais consistente.
3. **Foque na segurança:** Em aplicações relacionadas à saúde, é importante evitar informações inventadas e orientações inadequadas.
4. **Teste cenários reais:** Simule perguntas que uma pessoa usuária faria de verdade.
5. **Registre os resultados:** A avaliação ajuda a identificar pontos fortes e oportunidades de melhoria.
6. **Seja direto no pitch:** 3 minutos passam rápido; apresente o problema, a solução e o funcionamento de forma objetiva.

---

## Repositório Base do Desafio

Este projeto foi desenvolvido a partir do desafio **Construa Seu Assistente Virtual Com Inteligência Artificial**, da DIO.

📚 **Repositório Base:**  
[https://github.com/digitalinnovationone/dio-lab-bia-do-futuro](https://github.com/digitalinnovationone/dio-lab-bia-do-futuro)

📚 **Repositório de Exemplo:**  
[https://github.com/falvojr/dio-lab-bia-do-futuro](https://github.com/falvojr/dio-lab-bia-do-futuro)

---

## Projeto

O **DengueBot** demonstra uma aplicação de Inteligência Artificial Generativa integrada a uma base de conhecimento local e uma interface conversacional.

O projeto foi desenvolvido como um protótipo educacional, aplicando os conceitos propostos pelo desafio em um contexto relacionado à **saúde, tecnologia, dados e Inteligência Artificial**.

> **Importante:** O DengueBot é um assistente educativo e não substitui profissionais ou serviços de saúde. Não realiza diagnósticos, não prescreve medicamentos e não define tratamentos.
