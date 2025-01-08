
from data_validation.data_validation import DataValidation
from data_quality.data_quality import DataQuality
from data_process.data_process import Data_Process
import pandas as pd
import numpy as np


class DataPipeline:

    def __init__(self,path):
        self.path ='/home/ikaro/ETH_1min/data/raw/ETHUSD_1m_Binance.csv'
    
    def load_df(self):
        data = {
            "Open time": pd.date_range("2025-01-01", periods=1000, freq="H").astype(str),
            "Open": np.random.uniform(1000, 2000, 1000).astype(np.float64),
            "High": np.random.uniform(1000, 2000, 1000).astype(np.float64),
            "Low": np.random.uniform(1000, 2000, 1000).astype(np.float64),
            "Close": np.random.uniform(1000, 2000, 1000).astype(np.float64),
            "Volume": np.random.uniform(100, 500, 1000).astype(np.float64),
            "Close time": pd.date_range("2025-01-01 01:00", periods=1000, freq="H").astype(str),
            "Quote asset volume": np.random.uniform(10000, 50000, 1000).astype(np.float64),
            "Number of trades": np.random.randint(100, 500, 1000).astype(np.float64),
            "Taker buy base asset volume": np.random.uniform(50, 250, 1000).astype(np.float64),
            "Taker buy quote asset volume": np.random.uniform(5000, 25000, 1000).astype(np.float64),
            "Ignore": np.random.uniform(0, 1, 1000).astype(np.float64),
        }


        # df = pd.read_csv(self.path)
        df = pd.DataFrame(data)

        return df
        
    def pipe_line(self):
        df = self.load_df()
        validation = DataValidation(df)
        issues = validation.validate()
        print(issues)
        if issues['type_mismatches'] == {}:
            quality = DataQuality(df)
            df = quality.quality_control()
            print(df)
            process = Data_Process(df)
            df = process.enrichment()
            print(df)