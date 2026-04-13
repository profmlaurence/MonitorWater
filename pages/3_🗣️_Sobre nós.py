import streamlit as st

st.title("Equipe")

st.markdown("""
### Equipe do Projeto
- Dr. Thiago de Loiola - Coordenador
- Me. Moisés Laurence - Colaborador
- Me. Kelinne de Oliveira - Colaboradora
- Dr. Emerson Adriano Guarda - Colaborador
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



with st.expander("💻 Tecnologias e Bibliotecas Utilizadas"):
    st.markdown("""
    **🔌 Hardware e IoT**
    - **Arduino**: Microcontrolador para coleta de dados dos sensores de qualidade da água.

    **🌐 Aplicação Web**
    - **Streamlit**: Framework para desenvolvimento da aplicação web interativa.
    - **Plotly**: Biblioteca para construção de gráficos dinâmicos e interativos.

    **📊 Dados e Análise**
    - **Pandas**: Biblioteca para manipulação e análise de dados.
    - **KaggleHub**: Integração com datasets do Kaggle.

    **🤖 Aprendizado de Máquina**
    - **Scikit-learn**: Biblioteca para treinamento de modelos de classificação (Random Forest).
    - **Joblib**: Serialização e carregamento dos modelos treinados.

    **☁️ Deploy e Infraestrutura**
    - **Docker**: Containerização da aplicação.
    - **Google Cloud Run**: Hospedagem da aplicação na nuvem.
    """)