import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


class TimeSeriesForecast:
    def __init__(self, df, target_col, exog_cols=None):
        """
        df: DataFrame contendo dados ordenados por data no índice ou em uma coluna de data.
        target_col: nome da coluna que será prevista (ex: 'price_diff').
        exog_cols: lista de colunas que servem como variáveis exógenas (opcional).
        """
        self.df = df.copy()
        self.target_col = target_col
        self.exog_cols = exog_cols if exog_cols else []

        # Garante que o DataFrame esteja ordenado por data ou índice temporal
        self.df.sort_index(inplace=True)
        
    def train_test_split(self, split_ratio=0.8):
        """
        Separa os dados em treino e teste respeitando a ordem temporal.
        """
        split_point = int(len(self.df) * split_ratio)
        train_data = self.df.iloc[:split_point]
        test_data = self.df.iloc[split_point:]
        return train_data, test_data
    
    def fit_arima(self, order=(1,1,1), seasonal_order=None):
        """
        Ajusta um modelo ARIMA (ou SARIMA se seasonal_order for definido).
        order: parâmetros (p, d, q).
        seasonal_order: parâmetros (P, D, Q, m) para modelo sazonal.
        """
        # Se houver colunas exógenas, separar
        if self.exog_cols:
            exog_data = self.train[self.exog_cols]
        else:
            exog_data = None

        if seasonal_order:
            # Modelo SARIMA
            self.model = ARIMA(
                endog=self.train[self.target_col],
                exog=exog_data,
                order=order,
                seasonal_order=seasonal_order,
                enforce_stationarity=False,
                enforce_invertibility=False
            )
        else:
            # Modelo ARIMA simples
            self.model = ARIMA(
                endog=self.train[self.target_col],
                exog=exog_data,
                order=order,
                enforce_stationarity=False,
                enforce_invertibility=False
            )
        
        self.fitted_model = self.model.fit()
        return self.fitted_model

    def forecast(self, steps=None):
        """
        Faz previsões (forecast) para o conjunto de teste ou para o número de passos desejado.
        Se steps for None, faz previsões exatamente para o tamanho do conjunto de teste.
        """
        if steps is None:
            steps = len(self.test)
        
        # Se houver colunas exógenas, separar
        if self.exog_cols:
            exog_test = self.test[self.exog_cols].iloc[:steps]
        else:
            exog_test = None

        forecast_result = self.fitted_model.forecast(steps=steps, exog=exog_test)
        return forecast_result
    
    def run_pipeline(self, order=(1,1,1), seasonal_order=None, split_ratio=0.8):
        """
        Executa todo o fluxo: separa treino e teste, treina o ARIMA (ou SARIMA) e faz previsões.
        """
        self.train, self.test = self.train_test_split(split_ratio=split_ratio)
        
        self.fit_arima(order=order, seasonal_order=seasonal_order)
        
        preds = self.forecast()
        
        real = self.test[self.target_col].iloc[:len(preds)]
        rmse = np.sqrt(mean_squared_error(real, preds))
        
        print("Tamanho de treino:", len(self.train))
        print("Tamanho de teste:", len(self.test))
        print("RMSE no teste:", rmse)
        
        plt.figure(figsize=(10, 5))
        plt.plot(self.test.index[:len(preds)], real, label='Real', marker='o')
        plt.plot(self.test.index[:len(preds)], preds, label='Previsão', marker='x')
        plt.title(f'Previsão de {self.target_col} - ARIMA')
        plt.xlabel('Tempo')
        plt.ylabel(self.target_col)
        plt.legend()
        plt.show()