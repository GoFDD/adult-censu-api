import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from steps import Steps

class Trainer:
    def __init__(self):
        self.steps = Steps()

    def collect(self):
        return pd.read_csv("./data/adult_fe.csv")

    def train(self, df):
        x = df.copy()
        y = x.pop("income")
        x_train, _, y_train, _ = train_test_split(x, y, test_size=0.3, random_state=42)
        model = RandomForestClassifier(random_state=42)
        model.fit(x_train, y_train)
        return model

    def save(self, model):
        os.makedirs("./Models", exist_ok=True)
        with open("./Models/estimator.pkl", "wb") as f:
            pickle.dump(model, f)

    def run(self):
        if not os.path.isfile("./Models/estimator.pkl"):
            df = self.collect()
            df = self.steps.process(df)
            df = self.steps.engineer(df)
            df = self.steps.select(df)
            model = self.train(df)
            self.save(model)

if __name__ == "__main__":
    Trainer().run()