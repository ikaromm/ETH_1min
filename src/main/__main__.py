from data_pipeline.data_pipeline import DataPipeline
from machine_learn.machine_learn import Machine_Learn
def main():
  
    pipe_line = DataPipeline('teste')
    df = pipe_line.pipe_line()
    ml = Machine_Learn(df)
    ml.machine_learn()



if __name__ == "__main__":
    main()
