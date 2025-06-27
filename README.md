# API de Classificação de Qualidade da Laranja

Este projeto usa Machine Learning para prever a qualidade de uma laranja com base em características físicas e químicas.

O pipeline foi treinado com um RandomForestClassifier, integrado ao FastAPI para servir previsões via HTTP.

---

## Funcionalidades

- Pré-processamento com Feature-engine e Scikit-Learn
- Transformação da variável alvo em classes discretas
- Pipeline salvo e carregado com Joblib
- API criada com FastAPI
- Endpoint para previsão da qualidade da fruta

---

## 🛠️ Como executar localmente

Clone este repositório:

```bash
git clone git@github.com:Kevelee02/Laranjal-modelo.git
cd Laranjal-modelo
Crie um ambiente virtual e ative:

bash
    python3 -m venv venv
    source venv/bin/activate


Instale as dependências:
    pip install -r requirements.txt
    Inicie a API:

bash
  uvicorn api:app --reload
  Acesse a documentação interativa:
```

👉 http://127.0.0.1:8000/docs

🎯 Como fazer previsões
Use o endpoint /predict no Swagger UI ou envie um POST com dados JSON, exemplo:

json
{
  "Size": 7.1,
  "Weight": 120,
  "Brix": 13.2,
  "pH": 3.5,
  "Softness": 4,
  "HarvestTime": 30,
  "Ripeness": 5,
  "Color": "Orange",
  "Variety": "Navel",
  "Blemishes": 1
}
Resposta esperada:

json
{
  "Qualidade Prevista": 3
}

## O projeto foi desenvolvido com as seguintes etapas principais:

# Exploração dos dados:

    Visualização de distribuições e correlações com Seaborn e Matplotlib.

    Identificação de variáveis categóricas e numéricas.

    Detecção e tratamento de valores faltantes e outliers.

# Pré-processamento:

    Codificação de variáveis categóricas com One-Hot Encoding.

    Transformação da coluna de defeitos em binária (Blemishes).

    Padronização dos dados numéricos com StandardScaler.

    Conversão da variável alvo (contínua) em faixas discretas de qualidade.

# Modelagem:

    Treinamento de um RandomForestClassifier com ajuste de hiperparâmetros via Grid Search.

    Avaliação com métricas de acurácia e F1-score ponderado devido ao desbalanceamento entre classes.

    Análise da matriz de confusão para verificar o desempenho em cada classe.

# Empacotamento:

    Criação de um pipeline completo com scikit-learn e feature-engine.

    Salvamento do pipeline treinado em .pkl com joblib para posterior carregamento.

# Serviço de API:

    Implementação de uma API REST com FastAPI.

    Endpoint /predict para receber dados em JSON e retornar a qualidade prevista.

## Tecnologias utilizadas
    Python

    Scikit-Learn

    Feature-engine

    FastAPI

    Uvicorn

    Joblib
