import pickle
import pandas as pd
from steps import Steps

class Predictor:
    def __init__(self):
        self.steps = Steps()
        self.estimator = self.load_estimator()
        self.encoders = self.load_encoders()
        self.scaler = self.load_scaler()

    def load_estimator(self):
        with open("./Models/estimator.pkl", "rb") as f:
            return pickle.load(f)

    def load_encoders(self):
        with open("./Models/encoders.pkl", "rb") as f:
            return pickle.load(f)

    def load_scaler(self):
        with open("./Models/escalador.pkl", "rb") as f:
            return pickle.load(f)

    def predict(self, df):
        colunas_categoricas = ['marital.status', 'occupation']
        colunas_numericas = ['age', 'education.num', 'hours.per.week', 'capital.gain']

        for col in colunas_categoricas:
            if col in df.columns and col in self.encoders:
                le = self.encoders[col]
                df[col] = df[col].apply(lambda x: x if x in le.classes_ else 'Desconhecido')
                df[col] = le.transform(df[col].astype(str))

        colunas_numericas_presentes = [col for col in colunas_numericas if col in df.columns and df[col].notna().all()]
        if colunas_numericas_presentes:
            df[colunas_numericas_presentes] = self.scaler.transform(df[colunas_numericas_presentes])

        return self.estimator.predict(df)

    def run(self, df: pd.DataFrame):
        df = self.steps.process(df)
        df = self.steps.engineer(df)
        df = self.steps.select(df, is_predict=True)
        pred = self.predict(df)
        return pred