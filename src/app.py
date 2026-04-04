import pandas as pd
import json
import requests
import streamlit as st

#======================
#CONFIG VISUAL
#======================

st.set_page_config(page_title="Spendfy", page_icon="💰", layout="centered")

#======================
#CONFIGURAÇÃO
#======================

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss:120b-cloud"

#======================
#CARREGAR DADOS
#======================

#CSVs
historico = pd.read_csv ("data/historico_atendimento.csv")
transacoes = pd.read_csv("data/transacoes.csv")

#JSON
with open("data/perfil_investidor.json", "r", encoding = "utf-8") as f:
  perfil = json.load(f)

with open("data/produtos_financeiros.json", "r", encoding = "utf-8") as f:
  produtos = json.load(f)

#======================
#MONTAR CONTEXTO
#======================

contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

#======================
#SYSTEM PROMPT
#======================

SYSTEM_PROMPT = """
Você é o "Spendfy", um especialista financeiro amigável e didático.

Seu objetivo é educar o usuário financeiramente e ajudar a controlar os gastos durante o mês, fazendo com que ele possa ter um maior controle com os seus gastos. 

REGRAS:
01 - Nunca faça recomendações de investimentos. Apenas explique como cada uma funciona, mas não direcione o usuário a fazer tal investimento.
02 - Utilize apenas os dados fornecidos pelo usuário. Nunca invente caso não sabia de alguma informação.
03 - Caso não saiba de algo, admita e guie a conversa de forma simples. Por ex.: "Eu não tenho essa informação, mas posso te ajudar em..."
04 - Seja sempre amigável e carismático. Nunca utilize palavras ofensivas e/ou de baixo calão. Nunca falte com respeito com o usuário.
05 - Converse sempre com palavras simples, nada muito técnico para que o usuário possa entender com facilidade. 
06 - Seja sempre amigável e coerente. Nunca julgue os gastos do usuário.
"""

#======================
#CHAMAR O OLLAMA
#======================

def perguntar(msg):
  prompt = f"""
  {SYSTEM_PROMPT}

  CONTEXTO DO CLIENTE:
  {contexto}

  Pergunta: {msg}
  """

  try:
    r = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False
        }
    )

    data = r.json()

    if 'response' in data:
        return data['response']
    else:
        return f"Erro na API: {data}"

  except Exception as e:
    return f"Erro na requisição: {str(e)}"

#======================
#SIDEBAR
#======================

with st.sidebar:
    st.title("💰 Spendfy")
    st.markdown("Seu assistente financeiro inteligente!")

    st.divider()

    if st.button("🗑️ Limpar conversa"):
        st.session_state.messages = []
        st.rerun()

#======================
#ESTADO DE SESSÃO
#======================

if "messages" not in st.session_state:
    st.session_state.messages = []

#======================
#HEADER
#======================

st.title("💰 Spendfy, Sua Parceria Nas Despesas")
st.caption("Organize seus gastos de forma simples e inteligente!")

#======================
#CARDS DO CLIENTE
#======================

col1, col2 = st.columns(2)

col1.metric("Patrimônio", f"R$ {perfil['patrimonio_total']}")
col2.metric("Reserva", f"R$ {perfil['reserva_emergencia_atual']}")


#======================
#MENSAGEM INICIAL
#======================

if not st.session_state.messages:
    st.chat_message("assistant").write(
        "Olá! Eu sou o Spendfy 💰\n\n"
        "Posso te ajudar a entender seus gastos e organizar sua vida financeira.\n\n"
        "O que você quer analisar hoje?"
    )

#======================
#HISTÓRICO DE CHAT
#======================

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

#========
#INTERFACE
#========

if pergunta := st.chat_input("Pergunte alguma coisa..."):
    st.session_state.messages.append({"role": "user", "content": pergunta})
    st.chat_message("user").write(pergunta)

    with st.spinner("Analisando suas finanças... 💭"):
        resposta = perguntar(pergunta)

    st.session_state.messages.append({"role": "assistant", "content": resposta})
    st.chat_message("assistant").write(resposta)
