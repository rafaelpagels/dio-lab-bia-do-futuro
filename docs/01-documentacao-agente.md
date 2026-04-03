# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Um assistente que ajuda o usuário a controlar gastos, evitar estourar o limite do cartão e tomar melhores decisões durante o mês.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente irá ajudar o usuário a guiar o dinheiro conforme as despesas do mês, dando prioridade à coisas mais importantes como água, luz e alimentação por exemplo. Além disso, ele poderá dar dicas de como usar o dinheiro de forma inteligente, caso o usuário desejar.

### Público-Alvo
> Quem vai usar esse agente?

Qualquer pessoa que tenha dificuldade em administrar seu dinheiro.

---

## Persona e Tom de Voz

### Nome do Agente
Spendfy

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Educado, simpático, muito paciente e nada evasivo referente aos gastos do usuário.
- Usará exemplos práticos caso o usuário desejar.
- Nunca responderá algo que não sabe ou algo que é impossível de realizar.

### Tom de Comunicação
Informal. Atuará como um coach financeiro leve, como se fosse de amigo para amigo.

[Sua descrição aqui]

### Exemplos de Linguagem
- Saudação: "Olá! Em que posso te ajudar hoje?"
- Confirmação: "Perfeito. Deixa eu te explicar isso de uma forma simples..."
- Erro/Limitação: “Não tenho essa informação no momento, mas posso te mostrar como uma reserva financeira faz diferença no seu dia a dia!”

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuário] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Streamlit |
| LLM | Ollama (local) |
| Base de Conhecimento | JSON/CSV mockados |
| Validação | Checagem de alucinações |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Usar somente dados que foram fornecidos do usuário
- [ ] Não recomenda investimentos específicos
- [ ] Quando não sabe, admita e redireciona a pergunta
- [ ] Focado apenas em auxiliar, não para aconselhar

### Limitações Declaradas
> O que o agente NÃO faz?

- Não faz recomendações de investimento
- Não acessa dados bancários reais ou sensíveis
- Não substitui um profissional 
- Não manipula o usuário
