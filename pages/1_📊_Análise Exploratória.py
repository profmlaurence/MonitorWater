import kagglehub
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.plotting import WaterQualityPlotter
from utils.data import get_data, get_data_name, get_data_info


st.set_page_config(page_title="MonitorWater - Análise Exploratória", page_icon="📊", layout="wide")

# ── Cabeçalho ────────────────────────────────────────────────────────────────
st.title("📊 Análise Exploratória de Dados (EDA)")
st.caption("Explore as propriedades físico-químicas do dataset de potabilidade da água.")

# ── Dados ─────────────────────────────────────────────────────────────────────
df = get_data()
plotter = WaterQualityPlotter()
features = df.columns.drop('Potability')

# ── Métricas rápidas ──────────────────────────────────────────────────────────
total = len(df)
potable = int(df['Potability'].sum())
not_potable = total - potable

col_m1, col_m2, col_m3, col_m4 = st.columns(4)
col_m1.metric("Total de Amostras", f"{total:,}")
col_m2.metric("Potáveis", f"{potable:,}", f"{potable / total:.1%}")
col_m3.metric("Não Potáveis", f"{not_potable:,}", f"{not_potable / total:.1%}", delta_color="inverse")
col_m4.metric("Nº de Propriedades", len(features))

st.write("Dados: Kaggle Hub - ["+get_data_name()+"](https://www.kaggle.com/datasets/adityakadiwal/water-potability)")

with st.expander("🔎 Amostra dos dados brutos"):
    st.dataframe(df, width='stretch')

st.divider()

st.warning("Gráficos são melhores visualizados em computadores.")

# ── Navegação pelo Sidebar ──────────────────────────────────────────────────────
st.sidebar.header("Selecione o Gráfico")
secao = st.sidebar.selectbox("Categoria de visualização:", [
    "📋 Visão Geral",
    "📈 Distribuições",
    "🔗 Análise Multivariada",
    "🧪 Avançado",
])
# ═══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 1 — Visão Geral
# ═══════════════════════════════════════════════════════════════════════════════
if secao == "📋 Visão Geral":
    # st.sidebar.subheader("Subseção")
    subsecao = st.sidebar.radio("Escolha o gráfico:", ["🚰 Proporção de Potabilidade", "🧮 Mapa de Correlação"])
    
    if subsecao == "🚰 Proporção de Potabilidade":
        st.subheader("Quantas amostras de água são potáveis?")
        st.markdown(
            "O gráfico de rosca abaixo mostra a proporção entre amostras "
            "potáveis e não potáveis no dataset."
        )
        plotter.plot_potability_pie(df['Potability'].value_counts())
    
    elif subsecao == "🧮 Mapa de Correlação":
        st.subheader("Correlação entre Variáveis")
        st.markdown(
            "O mapa de calor abaixo mostra a correlação de Pearson entre as "
            "diversas propriedades da água. Valores próximos de **+1** ou **-1** "
            "indicam relações lineares fortes."
        )
        plotter.plot_correlation_heatmap(df)

# ═══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 2 — Distribuições
# ═══════════════════════════════════════════════════════════════════════════════
elif secao == "📈 Distribuições":
    # st.sidebar.subheader("Subseção")
    subsecao = st.sidebar.radio("Escolha o gráfico:", ["📊 Histograma + Box Plot", "🎻 Gráfico Violino"])
    
    if subsecao == "📊 Histograma + Box Plot":
        st.subheader("Histograma + Box Plot", help='O histograma mostra a distribuição de frequência dos dados, enquanto o box plot mostra a mediana, os quartis e os outliers.')
        feat_hist = st.selectbox(
            "Selecione a propriedade:", features, key="dist_selectbox"
        )
        plotter.plot_feature_distribution(df, feat_hist)
    
    elif subsecao == "🎻 Gráfico Violino":
        st.subheader("Gráfico Violino", help='O formato do "violino" evidencia distribuições bimodais e outliers com mais riqueza que um boxplot comum.')
        feat_violin = st.selectbox(
            "Selecione a propriedade:", features, key="violin_selectbox"
        )
        plotter.plot_violin(df, feat_violin)

# ═══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 3 — Análise Multivariada
# ═══════════════════════════════════════════════════════════════════════════════
elif secao == "🔗 Análise Multivariada":
    # st.sidebar.subheader("Subseção")
    subsecao = st.sidebar.radio("Escolha o gráfico:", ["🛤️ Coordenadas Paralelas", "🕸️ Gráfico de Radar", "🌌 Matriz de Dispersão"])
    
    if subsecao == "🛤️ Coordenadas Paralelas":
        st.subheader("Coordenadas Paralelas")
        st.caption(
            "Cada linha representa uma amostra passando por todos os eixos. "
            "Ajuda a encontrar padrões e faixas de valores associados à potabilidade."
        )
        plotter.plot_parallel_coordinates(df)
        
    elif subsecao == "🕸️ Gráfico de Radar":
        st.subheader("Gráfico de Radar (Spider Chart)")
        st.caption(
            "Assinatura visual usando a média normalizada de cada propriedade. "
            "Permite uma comparação holística rápida entre água Potável e Não Potável."
        )
        plotter.plot_spider_chart(df)
        
    elif subsecao == "🌌 Matriz de Dispersão":
        st.subheader("Matriz de Dispersão")
        st.caption(
            "Visão cruzada de todas as propriedades entre si, coloridas por potabilidade."
        )
        plotter.plot_scatter_matrix(df)

# ═══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 4 — Avançado
# ═══════════════════════════════════════════════════════════════════════════════
elif secao == "🧪 Avançado":
    # st.sidebar.subheader("Subseção")
    subsecao = st.sidebar.radio("Escolha o gráfico:", ["🧊 Dispersão 3D"])
    
    if subsecao == "🧊 Dispersão 3D":
        st.subheader("Dispersão 3D",help="Explore a relação entre três propriedades da água em um espaço tridimensional.")
        st.caption("Selecione 3 propriedades para explorar clusters espaciais interativamente.")

        col1, col2, col3 = st.columns(3)
        with col1:
            x_3d = st.selectbox(
                "Eixo X:", features,
                index=list(features).index('ph') if 'ph' in features else 0,
                key='3d_x',
            )
        with col2:
            y_3d = st.selectbox(
                "Eixo Y:", features,
                index=list(features).index('Hardness') if 'Hardness' in features else 1,
                key='3d_y',
            )
        with col3:
            z_3d = st.selectbox(
                "Eixo Z:", features,
                index=list(features).index('Sulfate') if 'Sulfate' in features else 2,
                key='3d_z',
            )
        plotter.plot_3d_scatter(df, x=x_3d, y=y_3d, z=z_3d)