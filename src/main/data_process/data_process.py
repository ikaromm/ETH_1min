import pandas as pd

class Data_Process:
    def __init__(self, df):
        self.df = df
    
    def enrich_data(self):
        """Cria novas colunas de enriquecimento."""
        # 1. Diferença de preço (Close - Open)
        self.df["price_diff"] = self.df["Close"] - self.df["Open"]
        
        # 2. Amplitude de preço (High - Low)
        self.df["price_range"] = self.df["High"] - self.df["Low"]
        
        # 3. Variação percentual ((Close - Open) / Open) * 100
        self.df["variation_pct"] = ((self.df["Close"] - self.df["Open"]) / self.df["Open"]) * 100
        
        # 4. Preço típico ((High + Low + Close) / 3)
        self.df["typical_price"] = (self.df["High"] + self.df["Low"] + self.df["Close"]) / 3
        
        # 5. Volume financeiro (Close * Volume)
        self.df["financial_volume"] = self.df["Close"] * self.df["Volume"]
        
        # 6. Índice de compra do Taker (Taker buy base asset volume / Volume)
        self.df["taker_buy_ratio"] = self.df["Taker buy base asset volume"] / self.df["Volume"]
        
        return self.df

    def add_moving_average(self, column="Close", window=7):
        """Adiciona coluna de média móvel simples para um período especificado."""
        ma_column_name = f"ma_{window}_{column}"
        self.df[ma_column_name] = self.df[column].rolling(window=window).mean()
        return self.df
      
    def enrichment(self):
      self.df = self.enrich_data()
      self.df = self.add_moving_average()
      self.df = self.add_moving_average(window=21)
      self.df = self.add_moving_average(window=63)
      
      return self.df
    
