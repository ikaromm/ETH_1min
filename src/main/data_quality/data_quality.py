import pandas as pd


class DataQuality:

    def __init__(self, df):
        self.df = df

    def delete_negative_values_by_column(self):
        self.df = self.df[
            (self.df["Open"] >= 0)
            & (self.df["High"] >= 0)
            & (self.df["Low"] >= 0)
            & (self.df["Close"] >= 0)
            & (self.df["Volume"] >= 0)
            & (self.df["Number of trades"] >= 0)
        ]
        return self.df

    def ignore_missing_values(self):
        self.df = self.df.dropna()
        return self.df

    def drop_duplicates(self):
        self.df = self.df.drop_duplicates(subset=["Open time"])
        return self.df

    def quality_control(self):
        self.df = self.delete_negative_values_by_column()
        self.df = self.ignore_missing_values()
        self.df = self.drop_duplicates()
        return self.df
