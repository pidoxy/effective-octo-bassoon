from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version

app = FastAPI()

class TextIn(BaseModel):
    features:str

class PredictionOut(BaseModel):
    result:str

app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}

app.post("/predict/{feature}", response_model=PredictionOut)
def predict(payload: TextIn):
    result = predict_pipeline(payload.text)
    return {"result": result}
