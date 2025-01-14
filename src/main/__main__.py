from data_pipeline.data_pipeline import DataPipeline
from machine_learn.machine_learn import Machine_Learn
from time_series.time_series import TimeSeriesForecast
def main():
  
    pipe_line = DataPipeline('teste')
    df = pipe_line.pipe_line()
    
    ml = Machine_Learn(df)
    ml.machine_learn()

    tm_series = TimeSeriesForecast(df, target_col="price_diff")
    tm_series.run_pipeline(order=(1,1,1))



if __name__ == "__main__":
    main()
