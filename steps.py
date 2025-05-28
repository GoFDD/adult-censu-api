import pandas as pd

class Steps:
    def process(self, df: pd.DataFrame):
        print("Colunas após process:", df.columns.tolist())
        return df

    def engineer(self, df: pd.DataFrame):
        return df

    def select(self, df: pd.DataFrame, is_predict=False):
        cols = ['age', 'education.num', 'marital.status', 'occupation', 'hours.per.week', 'capital.gain']
        if not is_predict:
            cols.append('income')
        cols_presentes = [col for col in cols if col in df.columns]
        return df[cols_presentes]