from data_validation.data_validation import DataValidation
import pandas as pd

def main():
  path_eth = '/home/ikaro/ETH_1min/data/raw/ETHUSD_1m_Binance.csv'
  df = pd.read_csv(path_eth)
  validation = DataValidation(df)
  issues = validation.validate()
  print(issues)
  
if __name__ == "__main__":
    main()
    # Chamadas de função, prints, etc.
