import streamlit as st
from pathlib import Path

import os

# Verificação de ambiente: local busca na pasta 'assets' a partir da raiz, nuvem usa Path(__file__)
if os.path.isdir("assets") or os.environ.get("STREAMLIT_SHARING_MODE"):
    BASE_DIR = Path(".") if os.path.isdir("assets") and not os.environ.get("STREAMLIT_SHARING_MODE") else Path(__file__).resolve().parent
else:
    BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(page_title="MonitorWater - Home", page_icon="🏠", layout="wide", initial_sidebar_state="expanded")

st.title("🚰 MonitorWater")
st.logo(str(BASE_DIR / "assets" / "logo-ifto.png"))

st.markdown("""
Este é um protótipo do sistema de monitoramento de qualidade da água, que deverá compor o ecossistema de 
monitoramento ambiental inteligente  do IFTO - Campus Araguatins.

Neste módulo é possível visualizar a qualidade da água e fazer previsões de potabilidade.
""")

st.info("Use o menu lateral para navegar entre as funcionalidades.")

col1, col2, col3, col4, col5= st.columns([1,2,2,2, 1])

with col2:
    if st.button("📊 Análise Exploratória", width='stretch', type='secondary'):
        st.switch_page("pages/1_📊_Análise Exploratória.py")
with col3:
    if st.button("🖥️ Monitoramento", width='stretch', type='secondary'):
        st.switch_page("pages/2_🖥️_Monitoramento.py")
with col4:
    if st.button("🧪 Previsão", width='stretch', type='secondary'):
        st.switch_page("pages/2_🧪_Previsão.py")

st.markdown("""
<p style='text-align: center; font-weight: 400; font-size: 12px;padding-top: 30px;'>
    Projeto em desenvolvimento proposto por Prof. Dr. Thiago de Loiola 
    em parceria com Laboratório de Pesquisa em Química Ambiental e de Biocombustíveis (Lapeq)
</p>""", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns([1,2,2,1])


with col2:
    st.image(str(BASE_DIR / "assets" / "logo-ifto.png"), width=80)
with col3:
    st.image(str(BASE_DIR / "assets" / "logo-lapeq.jpg"), width=80)
