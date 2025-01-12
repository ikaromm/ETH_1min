import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class Machine_Learn:
    def __init__(self, df):
        self.df = df

    def machine_learn(self):

        self.df["target"] = (self.df["price_diff"].shift(-1) > 0).astype(int)
        
        # Selecionar features e remover linhas com NaN
        features = ["price_diff", "price_range",
                     "variation_pct", "typical_price",
                       "financial_volume", "taker_buy_ratio"]
        
        data = self.df.dropna(subset=features + ["target"])

        X = data[features]
        y = data["target"]
        
        # Dividir em conjuntos de treino e teste sem embaralhar a ordem temporal
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=False)
        
        # Treinar um modelo de RandomForest para classificação
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Previsões e avaliação
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        print(f"Precisão do modelo: {accuracy:.2f}")
        
        return model
