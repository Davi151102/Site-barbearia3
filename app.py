import streamlit as st
from datetime import datetime, date

# Configuração da página (Estilo App)
st.set_page_config(page_title="InBarber Clone", page_icon="✂️")

# Estilização Customizada para parecer o InBarber
st.markdown("""
    <style>
    .main { background-color: #121212; color: white; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #EAB308; color: black; font-weight: bold; border: none; }
    .stSelectbox, .stDateInput { background-color: #1E1E1E !important; }
    </style>
    """, unsafe_allow_html=True)

# --- BANCO DE DADOS SIMULADO ---
SERVICOS = {
    "Corte Degradê": 45.00,
    "Barba": 30.00,
    "Combo (Corte + Barba)": 70.00,
    "Sobrancelha": 15.00
}

BARBEIROS = ["João da Navalha", "Lucas Barber", "Mestre VIP"]

HORARIOS = [
    "09:00", "09:30", "10:00", "10:30", "11:00", 
    "14:00", "14:30", "15:00", "15:30", "16:00"
]

# --- INTERFACE DO USUÁRIO ---
st.title("✂️ InBarber - Agendamento")
st.subheader("Reserve seu horário instantaneamente")

with st.container():
    st.write("---")
    
    # Passo 1: Escolha do Profissional
    barbeiro_fixo = st.selectbox("Selecione o Barbeiro", BARBEIROS)
    
    # Passo 2: Escolha do Serviço
    servico_escolhido = st.selectbox("O que vamos fazer hoje?", list(SERVICOS.keys()))
    preco = SERVICOS[servico_escolhido]
    st.info(f"Valor do serviço: R$ {preco:.2f}")

    # Passo 3: Data e Hora
    col1, col2 = st.columns(2)
    with col1:
        data_agendamento = st.date_input("Data", min_value=date.today())
    with col2:
        hora_agendada = st.selectbox("Horário", HORARIOS)

    st.write("---")

    # Passo 4: Dados do Cliente
    nome_cliente = st.text_input("Seu Nome")
    whatsapp_cliente = st.text_input("Seu WhatsApp (com DDD)")

    # Botão de Confirmação
    if st.button("CONFIRMAR AGENDAMENTO"):
        if nome_cliente and whatsapp_cliente:
            # Lógica de Confirmação
            resumo = (
                f"*AGENDAMENTO REALIZADO!* \n\n"
                f"👤 *Cliente:* {nome_cliente}\n"
                f"✂️ *Serviço:* {servico_escolhido}\n"
                f"🧔 *Barbeiro:* {barbeiro_fixo}\n"
                f"📅 *Data:* {data_agendamento.strftime('%d/%m/%Y')}\n"
                f"⏰ *Hora:* {hora_agendada}\n"
                f"💰 *Total:* R$ {preco:.2f}"
            )
            
            st.success("Agendamento salvo com sucesso!")
            st.code(resumo) # Mostra o comprovante
            
            # Criar link direto para o seu WhatsApp avisando do agendamento
            # Substitua o número abaixo pelo seu número real
            seu_numero = "5511999999999" 
            link_whatsapp = f"https://wa.me/{seu_numero}?text={resumo.replace('*', '').replace(' ', '%20')}"
            st.markdown(f"[Notificar Barbeiro via WhatsApp]({link_whatsapp})")
        else:
            st.error("Por favor, preencha seu nome e telefone.")

# Rodapé
st.markdown("<br><p style='text-align: center; color: gray;'>Powered by Python - InBarber System</p>", unsafe_allow_html=True)
