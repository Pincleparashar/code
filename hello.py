import numpy as np
import pandas as pd

print("Hellp world!!")

def create_df(row, column):
    return pd.DataFrame(np.random.randn(row, column),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])

print(create_df(10, 4))