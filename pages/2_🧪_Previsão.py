import streamlit as st
import pandas as pd
import joblib
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.data import get_data

st.set_page_config(page_title="MonitorWater - Previsão", page_icon="🧪", layout="wide")

st.title("🧪 Previsão de Potabilidade")
st.markdown("Ajuste os parâmetros abaixo para simular as propriedades da água e descobrir se ela é segura para consumo humano (Potável).")

df = get_data()

@st.cache_resource
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'best_model.pkl')
    return joblib.load(model_path)

try:
    model = load_model()
except Exception as e:
    st.warning("⚠️ O modelo ainda não foi treinado. Por favor, aguarde o treinamento (execute `python models/train.py`).")
    st.stop()

col1, col2, col3 = st.columns(3)

def create_input(col, feature):
    min_val = float(df[feature].min())
    max_val = float(df[feature].max())
    mean_val = float(df[feature].mean())
    return col.slider(feature, min_value=min_val, max_value=max_val, value=mean_val)

input_data = {}
features = df.columns.drop('Potability')

for i, feature in enumerate(features):
    c = [col1, col2, col3][i % 3]
    input_data[feature] = create_input(c, feature)

if st.button("Avaliar Potabilidade", width='stretch', type="primary"):
    with st.spinner("Analisando propriedades..."):
        input_df = pd.DataFrame([input_data])
        prediction = model.predict(input_df)[0]
        prob = model.predict_proba(input_df)[0]
        
        st.markdown("---")
        if prediction == 1:
            st.success(f"### 💧 **Água Potável**! \nEssa amostra de água foi classificada como própria para consumo.\n\n**Confiança:** {prob[1]*100:.2f}%")
        else:
            st.error(f"### ☠️ **Água Não Potável**! \nEssa amostra de água NÃO é segura para consumo.\n\n**Confiança:** {prob[0]*100:.2f}%")
