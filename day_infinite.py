import pandas as pd
import numpy as np

data = {
    'id': [101, 102, 103, 104, 105, 101, 103, 106],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Alice', 'Charlie', 'Frank'],
    'age': [25, 30, 35, 40, 22, 25, 36, 29],
    'city': ['New York', 'Paris', 'London', 'Berlin', 'Paris', 'New York', 'London', 'Tokyo']
}

df = pd.DataFrame(data)
df = df.drop_duplicates()
print(df)