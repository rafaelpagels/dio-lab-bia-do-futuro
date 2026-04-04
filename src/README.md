# Passo a Passo de Execução

## Setup do Ollama

```bash
#1. Instalar Ollama (ollama.com)
#2. Baixar um modelo leve
ollama pull gpt-oss
ou
use o modelo gpt-oss:120b em núvem, como no caso desse projeto. Para utilizar, basta abrir o terminal, digitar 'ollama signin' e fazer o login em sua conta

#3. Testar se funciona
ollama run gpt-oss "Olá!"
```

## Código Completo

Todo o código-fonte está no arquivo `app.py`

## Como Rodar

```bash
# 1. Instalar dependências
pip install streamlit pandas requests

# 2. Garantir que o Ollama está rodando
ollama serve

# 3. Rodar o app
streamlit run .\src\app.py
```

## Evidências

<img width="1901" height="906" alt="image" src="https://github.com/user-attachments/assets/e807366e-97de-4373-b384-19d6d92471ea" />

---

<img width="1901" height="906" alt="image" src="https://github.com/user-attachments/assets/c82d9536-3f91-49f9-8858-82d7323c4dc6" />


