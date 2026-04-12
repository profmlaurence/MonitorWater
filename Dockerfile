# Usar uma imagem oficial do Python
FROM python:3.11-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar o arquivo de dependências
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação
COPY . .

# Expor a porta que o Cloud Run necessita (a variável PORT é injetada automaticamente, default é 8080)
EXPOSE 8080

# Comando para rodar a aplicação Streamlit
CMD streamlit run 0_🏠_Home.py --server.port=${PORT:-8080} --server.address=0.0.0.0
