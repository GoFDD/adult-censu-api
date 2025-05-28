import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from trainer import Trainer
from predictor import Predictor
import logging
import os

app = FastAPI()


tr = Trainer()
tr.run()
pr = Predictor()

@app.get("/")
async def root():
    return {"message": "API para prever renda a partir de dados do Adult Censu"}

class Person(BaseModel):
    age: float
    education_num: float
    marital_status: str
    occupation: str
    hours_per_week: float
    capital_gain: float

class People(BaseModel):
    data: List[Person]

@app.post("/predict")
async def predict(people: People):
    try:
        df = pd.DataFrame([p.dict() for p in people.data])
        df.columns = ['age', 'education.num', 'marital.status', 'occupation', 'hours.per.week', 'capital.gain']
        preds = pr.run(df)
        return {"predictions": preds.tolist()}
    except Exception as e:
        logging.error("Erro na predição: %s", str(e))
        raise HTTPException(status_code=400, detail=f"Erro na predição: {str(e)}")