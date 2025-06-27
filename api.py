from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Carregar o modelo treinado
model = joblib.load('modelo_treinado.pkl')

@app.get("/")
def read_root():
    return {"Mensagem": "API de Predição de Qualidade de Laranja"}

@app.post("/predict/")
def predict_quality(
    Size: float,
    Weight: float,
    Brix: float,
    pH: float,
    Softness: float,
    HarvestTime: float,
    Ripeness: float,
    Color: str,
    Variety: str,
    Blemishes: int
):
    dados = pd.DataFrame([{
        'Size (cm)': Size,
        'Weight (g)': Weight,
        'Brix (Sweetness)': Brix,
        'pH (Acidity)': pH,
        'Softness (1-5)': Softness,
        'HarvestTime (days)': HarvestTime,
        'Ripeness (1-5)': Ripeness,
        'Color': Color,
        'Variety': Variety,
        'Blemishes (Y/N)': Blemishes
    }])

    prediction = model.predict(dados)

    return {"Qualidade_Prevista": int(prediction[0])}
