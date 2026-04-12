# 🚰 MonitorWater

Sistema de monitoramento de qualidade da água desenvolvido como protótipo para o ecossistema de monitoramento ambiental inteligente do **IFTO – Campus Araguatins**, em parceria com o **Laboratório de Pesquisa em Química Ambiental e de Biocombustíveis (LAPEQ)**.

A aplicação permite **visualizar**, **explorar** e **prever** a potabilidade de amostras de água com base em propriedades físico-químicas, utilizando técnicas de análise exploratória de dados e aprendizado de máquina.

---

## 📋 Funcionalidades

| Funcionalidade | Status |
|---|---|
| Análise Exploratória de Dados (EDA) | ✅ |
| Previsão de Potabilidade (ML) | ✅ |
| Monitoramento em Tempo Real | ☑️ Planejado |
| Alertas | ☑️ Planejado |
| Relatórios | ☑️ Planejado |
| Integração com IoT | ☑️ Planejado |
| Integração com Banco de Dados | ☑️ Planejado |
| Integração Cloud (GCP) | ✅ |
| Integração Web | ✅ |

---

## 📊 Visualizações Disponíveis

A página de **Análise Exploratória** oferece gráficos interativos organizados em abas:

- **Visão Geral** — Gráfico de rosca (potabilidade) e Heatmap de correlação
- **Distribuições** — Histograma + Box Plot e Gráfico Violino (lado a lado)
- **Análise Multivariada** — Coordenadas Paralelas, Radar (Spider Chart) e Matriz de Dispersão
- **Avançado** — Dispersão 3D interativa com seleção dinâmica de eixos

---

## 🧪 Previsão de Potabilidade

A página de **Previsão** permite ao usuário ajustar parâmetros físico-químicos da água via sliders interativos e obter uma classificação instantânea de potabilidade (Potável / Não Potável) com nível de confiança, usando um modelo de **Random Forest** treinado com `scikit-learn`.

## ⚙️ Tecnologias Utilizadas

- **[Streamlit](https://streamlit.io/)** — Framework para a interface web interativa
- **[Plotly](https://plotly.com/python/)** — Gráficos interativos (rosca, heatmap, violino, radar, 3D, etc.)
- **[Pandas](https://pandas.pydata.org/)** — Manipulação e análise de dados
- **[Scikit-learn](https://scikit-learn.org/)** — Treinamento do modelo de aprendizado de máquina
- **[KaggleHub](https://github.com/Kaggle/kagglehub)** — Download automático do dataset
- **[Joblib](https://joblib.readthedocs.io/)** — Persistência do modelo treinado

---

## 🚀 Como Executar Localmente

### Pré-requisitos

- Python 3.10+
- Conta no [Kaggle](https://www.kaggle.com/) (com API key configurada para download dos dados)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/<seu-usuario>/MonitorWater.git
cd MonitorWater

# Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
# .venv\Scripts\activate    # Windows

# Instale as dependências
pip install -r requirements.txt
```

### Treinamento do Modelo

```bash
python models/train.py
```

### Execução da Aplicação

```bash
streamlit run 0_🏠_Home.py
```

---

## ☁️ Deploy no Google Cloud Run

O projeto está preparado para deploy no **Google Cloud Run**. Consulte a documentação do GCP para configurar o `Dockerfile` e realizar o deploy via `gcloud run deploy`.

---

## 👥 Créditos

**Laboratório de Pesquisa em Química Ambiental e de Biocombustíveis (Lapeq)**.

---
## Equipe Executora

- **[Prof. Dr. Thiago de Loiola]** - [Coordenador do Projeto]
- **[Prof. Dr. Emerson Adriano Guarda]** - [Coordenador do LAPEQ]
- **[Prof. Me. Moisés Laurence]** - [Desenvolvedor]

