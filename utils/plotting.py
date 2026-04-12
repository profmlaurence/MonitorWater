import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

class WaterQualityPlotter:
    def __init__(self):
        self.colors_blue = ["#132C33", "#264D58", '#17869E', '#51C4D3', '#B4DBE9']
        self.colors_dark = ["#1F1F1F", "#313131", '#636363', '#AEAEAE', '#DADADA']
        self.colors_green = ['#01411C','#4B6F44','#4F7942','#74C365','#D0F0C0']

    def plot_potability_pie(self, d_potability):
        d_potability.name = 'Potability'
        fig = px.pie(d_potability,values='Potability',names=['Não Potável','Potável'],hole=0.4,opacity=0.6,
                color_discrete_sequence=[self.colors_green[3],self.colors_blue[3]],
                 labels={'label':'Potabilidade','Potability':'Nº de Amostras'})

        fig.add_annotation(text='Potabilidade',
                        x=0.5,y=0.5,showarrow=False,font_size=14,opacity=0.7,font_family='monospace')

        fig.update_layout(
            font_family='monospace',
            legend=dict(x=0.37,y=-0.05,orientation='h',traceorder='reversed'),
            hoverlabel=dict(bgcolor='white'),
            showlegend=True)

        fig.update_traces(textposition='outside', textinfo='percent+label')
       
        st.plotly_chart(fig, width='stretch')

    def plot_correlation_heatmap(self, df):
        corr = df.corr()
        fig = px.imshow(corr, text_auto=True, aspect="auto",
                        color_continuous_scale=self.colors_blue)
        fig.update_layout(title="Correlation Heatmap", font_family='monospace')
        st.plotly_chart(fig, width='stretch')

    def plot_feature_distribution(self, df, feature):
        df_copy = df.copy()
        df_copy['Potability'] = df_copy['Potability'].map({0: 'Não Potável', 1: 'Potável'})
        fig = px.histogram(df_copy, x=feature, color='Potability', marginal="box",
                           barmode="overlay", color_discrete_sequence=[self.colors_green[3], self.colors_blue[3]])
        fig.update_layout(title=f"Distribuição da propriedade {feature}", font_family='monospace')
        st.plotly_chart(fig, width='stretch')
    
    def plot_parallel_coordinates(self, df):
        fig = px.parallel_coordinates(
            df, 
            color="Potability",
            color_continuous_scale=[self.colors_green[3], self.colors_blue[3]],
            color_continuous_midpoint=0.5
        )
        st.plotly_chart(fig, width='stretch')

    def plot_scatter_matrix(self, df):
        fig = px.scatter_matrix(df,df.drop('Potability',axis=1),height=1250,width=1250,template='plotly_white',opacity=0.7,
                        color_discrete_sequence=[self.colors_blue[3],self.colors_green[3]],color='Potability',
                       symbol='Potability',color_continuous_scale=[self.colors_green[3],self.colors_blue[3]])

        fig.update_layout(font_family='monospace',font_size=10,
                  coloraxis_showscale=False,
                 legend=dict(x=0.02,y=1.07,bgcolor=self.colors_dark[4]),
                 title=dict(text='Scatter Plot Matrix b/w Features',x=0.5,y=0.97,
                   font=dict(color=self.colors_dark[2],size=24)))
        st.plotly_chart(fig, width='stretch')

    def plot_violin(self, df, feature):
        df_copy = df.copy()
        df_copy['Potability'] = df_copy['Potability'].map({0: 'Não Potável', 1: 'Potável'})
        fig = px.violin(df_copy, x='Potability', y=feature, color='Potability', box=True,
                        color_discrete_sequence=[self.colors_green[3], self.colors_blue[3]])
        fig.update_layout(title=f"Distribuição da propriedade {feature}", font_family='monospace')
        st.plotly_chart(fig, width='stretch')

    def plot_spider_chart(self, df):
        import pandas as pd
        features = df.columns.drop('Potability')
        # Normaliza entre 0 e 1 para que o Radar fique visualmente comparável
        df_norm = (df[features] - df[features].min()) / (df[features].max() - df[features].min())
        df_norm['Potability'] = df['Potability'].map({0: 'Não Potável', 1: 'Potável'})
        
        # Calcula a média por Potabilidade
        df_mean = df_norm.groupby('Potability').mean().reset_index()
        df_melt = pd.melt(df_mean, id_vars=['Potability'], var_name='Feature', value_name='Value')
        
        fig = px.line_polar(df_melt, r='Value', theta='Feature', color='Potability', line_close=True,
                            color_discrete_sequence=[self.colors_green[3], self.colors_blue[3]])
        fig.update_traces(fill='toself', opacity=0.6)
        fig.update_layout(title="Gráfico de Radar (Média Normalizada)", font_family='monospace')
        st.plotly_chart(fig, width='stretch')

    def plot_3d_scatter(self, df, x='ph', y='Hardness', z='Sulfate'):
        df_copy = df.copy()
        df_copy['Potability'] = df_copy['Potability'].map({0: 'Não Potável', 1: 'Potável'})
        fig = px.scatter_3d(df_copy, x=x, y=y, z=z, color='Potability',
                            color_discrete_sequence=[self.colors_green[3], self.colors_blue[3]], opacity=0.7)
        fig.update_layout(title=f"Dispersão 3D: {x} vs {y} vs {z}", font_family='monospace', height=700)
        st.plotly_chart(fig, width='stretch')

    def plot_density_contours(self, df, x='ph', y='Hardness'):
        df_copy = df.copy()
        df_copy['Potability'] = df_copy['Potability'].map({0: 'Não Potável', 1: 'Potável'})
        # Usa marginal="histogram" para ver a distribuição marginal junto com os contornos
        fig = px.density_contour(df_copy, x=x, y=y, color="Potability",
                                 color_discrete_sequence=[self.colors_green[3], self.colors_blue[3]], marginal_x="histogram", marginal_y="histogram")
        fig.update_traces(contours_coloring="fill", opacity=0.7, selector=dict(type='histogram2dcontour'))
        fig.update_layout(title=f"Contorno de Densidade: {x} vs {y}", font_family='monospace')
        st.plotly_chart(fig, width='stretch')