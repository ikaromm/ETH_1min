import pandas as pd 
import numpy as np

class DataValidation:
    def __init__(self, df):
        self.df = df
        self.issues = {}

    def check_missing_values(self):
        missing = self.df.isna().sum()
        self.issues["missing_values"] = missing[missing > 0].to_dict()
        return missing

    def check_data_types(self, expected_types):
        """expected_types é um dicionário, ex: {'Open time': 'datetime64[ns]', 'Open': 'float'}"""
        type_issues = {}
        for col, expected_type in expected_types.items():
            if col in self.df.columns:
                if self.df[col].dtype != expected_type:
                    type_issues[col] = {
                        "expected": expected_type,
                        "found": self.df[col].dtype,
                    }
        self.issues["type_mismatches"] = type_issues

    def check_duplicates(self):
        duplicates = self.df.duplicated().sum()
        self.issues["duplicates"] = duplicates
        return duplicates

    def validate(self):

        missing = self.check_missing_values()
        duplicates = self.check_duplicates()
        data_types = self.check_data_types(
            {
                "Open time": object,
                "Open": np.float64,
                "High": np.float64,
                "Low": np.float64,
                "Close": np.float64,
                "Volume": np.float64,
                "Close time": object,
                "Quote asset volume": np.float64,
                "Number of trades": np.float64,
                "Taker buy base asset volume": np.float64,
                "Taker buy quote asset volume": np.float64,
                "Ignore": np.float64,
            }
        )

        return self.issues

