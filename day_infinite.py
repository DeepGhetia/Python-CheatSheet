import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
    'Age': [25, np.nan, 30, 22, 28],
    'City': ['New York', 'Los Angeles', None, 'Chicago', 'Houston'],
    'Salary': [None, None, np.nan, None, None]
}

df = pd.DataFrame(data)
print(df.dropna(axis=0,how='all',subset=['Salary']))