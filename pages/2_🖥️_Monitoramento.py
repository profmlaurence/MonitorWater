from utils.data import get_data
import streamlit as st
import pandas as pd
import datetime
import streamlit.components.v1 as components
from numpy.random import default_rng as rng


st.set_page_config(page_title="MonitorWater - Monitoramento", page_icon="🖥️", layout="wide")

st.title("🖥️ Monitoramento")

# st.sidebar.header("Lista de Sensores")
# st.sidebar.subheader("Sensores ativos")
# st.sidebar.checkbox("🟩 Sensor 0", key='sensor_0')
# st.sidebar.checkbox("🟩 Sensor 1", key='sensor_1')
# st.sidebar.checkbox("🟩 Sensor 2", key='sensor_2')
# st.sidebar.checkbox("🟩 Sensor 3", key='sensor_3')

# st.sidebar.subheader("Sensores inativos")
# st.sidebar.checkbox("🟥 Sensor 4", key='sensor_4')
# st.sidebar.checkbox("🟥 Sensor 5", key='sensor_5')

st.sidebar.header("Gerenciamento de Sensores", divider='blue')
st.sidebar.button("Adicionar sensor", key='add_sensor')
st.sidebar.button("Remover sensor", key='remove_sensor')
st.sidebar.button("Editar sensor", key='edit_sensor')
st.sidebar.button("Salvar alterações", key='save_changes')


def gen_metrics(seed):
    df = get_data()
    ph = df['ph']
    hardness = df['Hardness']
    Chloramines = df['Chloramines']
    Solids = df['Solids']
    Turbidity = df['Turbidity']
    Potability = df['Potability']

    ph_mean = ph.mean()
    hardness_mean = hardness.mean()
    chloramines_mean = Chloramines.mean()
    solids_mean = Solids.mean()
    turbidity_mean = Turbidity.mean()
    potability_mean = Potability.mean()

    ph_chgs = list(rng(seed).normal(0, ph.std() / 10, 20))
    ph_dt = [ph_mean + sum(ph_chgs[:i]) for i in range(20)]
    ph_dlt = round(ph_dt[-1] - ph_mean, 2)

    hardness_chgs = list(rng(seed).normal(0, hardness.std() / 10, 20))
    hardness_dt = [hardness_mean + sum(hardness_chgs[:i]) for i in range(20)]
    hardness_dlt = round(hardness_dt[-1] - hardness_mean, 2)

    chloramines_chgs = list(rng(seed).normal(0, Chloramines.std() / 10, 20))
    chloramines_dt = [chloramines_mean + sum(chloramines_chgs[:i]) for i in range(20)]
    chloramines_dlt = round(chloramines_dt[-1] - chloramines_mean, 2)

    solids_chgs = list(rng(seed).normal(0, Solids.std() / 10, 20))
    solids_dt = [solids_mean + sum(solids_chgs[:i]) for i in range(20)]
    solids_dlt = round(solids_dt[-1] - solids_mean, 2)

    turbidity_chgs = list(rng(seed).normal(0, Turbidity.std() / 10, 20))
    turbidity_dt = [turbidity_mean + sum(turbidity_chgs[:i]) for i in range(20)]
    turbidity_dlt = round(turbidity_dt[-1] - turbidity_mean, 2)

    potability_chgs = list(rng(seed).normal(0, Potability.std() / 10, 20))
    potability_dt = [potability_mean + sum(potability_chgs[:i]) for i in range(20)]
    potability_dlt = round(potability_dt[-1] - potability_mean, 2)

    return ph_dt, ph_dlt, hardness_dt, hardness_dlt, chloramines_dt, chloramines_dlt, solids_dt, solids_dlt, turbidity_dt, turbidity_dlt, potability_dt, potability_dlt

def render_sensor(sensor_id, location, coord, is_active, battery):
    icon = "🟩" if is_active else "🟥"
    status_text = "Ativo" if is_active else "Inativo"
    battery_icon = "🔋" if battery >= 50 else "🪫"
    
    with st.expander(f"Sensor {sensor_id} {icon} - {location}", expanded=False):
        st.write(f"{battery_icon} Bateria: {battery}%")
        
        if is_active:
            now = datetime.datetime.now()
            current_time = now.strftime("%d/%m/%Y - %H:%M")
            next_maintenance = (now + datetime.timedelta(minutes=15)).strftime("%d/%m/%Y - %H:%M")
            
            st.write(f"Ultima atualização: {current_time}")
            st.write(f"Próxima manutenção: {next_maintenance}")
            
            df = get_data()

            (ph_dt, ph_dlt, hardness_dt, hardness_dlt, 
             chloramines_dt, chloramines_dlt, solids_dt, solids_dlt, 
             turbidity_dt, turbidity_dlt, potability_dt, potability_dlt) = gen_metrics(sensor_id)

            row = st.container(horizontal=True)
            with row:
                st.metric("pH", round(df['ph'].mean(), 2), ph_dlt, chart_data=ph_dt, chart_type="line", border=True)
                st.metric("Turbidity", round(df['Turbidity'].mean(), 2), turbidity_dlt, chart_data=turbidity_dt, chart_type="area", border=True)
                st.metric("Chloramines", round(df['Chloramines'].mean(), 2), chloramines_dlt, chart_data=chloramines_dt, chart_type="bar", border=True)
                st.metric("Hardness", round(df['Hardness'].mean(), 2), hardness_dlt, chart_data=hardness_dt, chart_type="line", border=True)
                st.metric("Solids", round(df['Solids'].mean(), 2), solids_dlt, chart_data=solids_dt, chart_type="area", border=True)

        st.subheader("📍 Mapa de Localização")
        st.map(
            data=pd.DataFrame(coord),
            zoom=13,
            color="#FF0000" if is_active else "#808080",
            size=40,
        )   
        st.divider()

# Dicionário de localidades
sensor_locations = {
    0: ("Psicultura 1 IFTO Araguatins", {'lat': [-5.640600], 'lon': [-48.073122]}, True, 90),
    1: ("Pov. Santa Tereza - Araguatins", {'lat': [-5.648895], 'lon': [-48.082465]}, True, 80),
    2: ("Fundo do Campus", {'lat': [-5.639581], 'lon': [-48.076610]}, True, 70),
    3: ("Psicultura 2 IFTO Araguatins", {'lat': [-5.640264], 'lon': [-48.072876]}, False, 0),
    4: ("Poço Artesiano IFTO Araguatins", {'lat': [-5.639078], 'lon': [-48.066487]}, True, 47),
    5: ("Rio Araguaia - Ponto 1", {'lat': [-5.638653], 'lon': [-48.128245]}, False, 40),
}

# Laço para renderizar apenas os sensores que estão selecionados na barra lateral
for i in range(6):
    render_sensor(i, sensor_locations[i][0], sensor_locations[i][1], sensor_locations[i][2], sensor_locations[i][3])

if st.session_state.add_sensor or st.session_state.remove_sensor or st.session_state.edit_sensor or st.session_state.save_changes:
    st.toast("🫧Funcionalidade em desenvolvimento.")