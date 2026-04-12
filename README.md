# 🚰 MonitorWater

Sistema de monitoramento de qualidade da água desenvolvido como protótipo para o ecossistema de monitoramento ambiental inteligente do **IFTO – Campus Araguatins**, em parceria com o **Laboratório de Química da UFT (LAPEQ)**.

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

---

## 🗂️ Estrutura do Projeto

```
MonitorWater/
├── 0_🏠_Home.py              # Página inicial da aplicação
├── pages/
│   ├── 1_📊_Análise Exploratória.py   # EDA com gráficos interativos
│   └── 2_🧪_Previsão.py               # Previsão de potabilidade (ML)
├── utils/
│   ├── data.py                # Carregamento de dados (Kaggle)
│   └── plotting.py            # Classe WaterQualityPlotter (Plotly)
├── models/
│   ├── train.py               # Script de treinamento do modelo
│   └── best_model.pkl         # Modelo treinado (Random Forest)
├── assets/                    # Logos e imagens
├── .gitignore
└── README.md
```

---

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

## 📄 Dataset

O dataset utilizado é o [**Water Potability**](https://www.kaggle.com/datasets/adityakadiwal/water-potability) disponível no Kaggle, contendo as seguintes propriedades:

| Propriedade | Descrição |
|---|---|
| `ph` | Potencial hidrogeniônico |
| `Hardness` | Dureza da água (mg/L) |
| `Solids` | Sólidos totais dissolvidos (ppm) |
| `Chloramines` | Cloraminas (ppm) |
| `Sulfate` | Sulfato (mg/L) |
| `Conductivity` | Condutividade elétrica (μS/cm) |
| `Organic_carbon` | Carbono orgânico total (ppm) |
| `Trihalomethanes` | Trihalometanos (μg/L) |
| `Turbidity` | Turbidez (NTU) |
| `Potability` | Potabilidade (0 = Não potável, 1 = Potável) |

---

## 👥 Créditos

Projeto proposto por **Prof. Dr. Thiago de Loiola** em parceria com o **Laboratório de Química da UFT (LAPEQ)**.

<p align="center">
  <strong>IFTO – Campus Araguatins</strong> &nbsp;•&nbsp; <strong>LAPEQ – UFT</strong>
</p>
