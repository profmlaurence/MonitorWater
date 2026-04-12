import streamlit as st

st.set_page_config(page_title="MonitorWater - Home", page_icon="🏠", layout="wide", initial_sidebar_state="expanded")

st.title("🚰 MonitorWater")
st.markdown("""
Este é um protótipo do sistema de monitoramento de qualidade da água, que deverá compor o ecossistema de 
monitoramento ambiental inteligente  do IFTO - Campus Araguatins.

Neste módulo é possível visualizar a qualidade da água e fazer previsões de potabilidade.

Use o menu lateral para navegar entre as funcionalidades.
""")
with st.expander("🛠️ Status das funcionalidades"):
    st.markdown("""
    ✅ Análise Exploratória de Dados (EDA)

    ✅ Previsão de Potabilidade

    ☑️ Monitoramento em Tempo Real

    ☑️ Alertas

    ☑️ Relatórios

    ☑️ Integração com IoT

    ☑️ Integração com Banco de Dados

    ✅ Integração com Cloud

    ☑️ Integração com Mobile

    ✅ Integração com Web
    """)



with st.expander("💻 Tecnologias e Biblioteca Utilizadas"):
    st.markdown("""
    - **Streamlit**: Framework para desenvolvimento da aplicação web.
    - **Pandas**: Biblioteca para manipulação e análise de dados.
    - **Scikit-learn**: Biblioteca para aprendizado de máquina.
    - **Matplotlib**: Biblioteca para visualização de dados.
    - **Seaborn**: Biblioteca para visualização de dados.
    """)

st.divider()

st.markdown("<p style='text-align: center; font-weight: 400; font-size: 12px;padding-top: 30px;'>Projeto em desenvolvimento proposto por Prof. Dr. Thiago de Loiola em parceria com Laboratório de Química da UFT (LAPEQ)</p>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns([1,2,2, 1])


with col2:
    st.image("assets/logo-ifto.png", width=80)
with col3:
    st.image("assets/logo-lapeq.jpg",  width=80)
