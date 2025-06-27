# 🍊 API de Classificação de Qualidade da Laranja

Este projeto usa Machine Learning para prever a qualidade de uma laranja com base em características físicas e químicas.

O pipeline foi treinado com um RandomForestClassifier, integrado ao FastAPI para servir previsões via HTTP.

---

## 🚀 Funcionalidades

- Pré-processamento com Feature-engine e Scikit-Learn
- Transformação da variável alvo em classes discretas
- Pipeline salvo e carregado com Joblib
- API criada com FastAPI
- Endpoint para previsão da qualidade da fruta

---

## 📂 Estrutura do projeto

Projeto001/
├── api.py # Código da API FastAPI
├── modelo_treinado.pkl # Pipeline treinado e salvo
├── requirements.txt # Dependências do projeto
├── README.md # Este arquivo
└── .gitignore

yaml
Copiar
Editar

---

## 🛠️ Como executar localmente

Clone este repositório:

```bash
git clone git@github.com:Kevelee02/Laranjal-modelo.git
cd Laranjal-modelo
Crie um ambiente virtual e ative:

bash
Copiar
Editar
python3 -m venv venv
source venv/bin/activate
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Inicie a API:

bash
Copiar
Editar
uvicorn api:app --reload
Acesse a documentação interativa:

👉 http://127.0.0.1:8000/docs

🎯 Como fazer previsões
Use o endpoint /predict no Swagger UI ou envie um POST com dados JSON, exemplo:

json
Copiar
Editar
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
Copiar
Editar
{
  "Qualidade Prevista": 3
}
💻 Tecnologias utilizadas
Python

Scikit-Learn

Feature-engine

FastAPI

Uvicorn

Joblib
