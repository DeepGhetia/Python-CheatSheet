import pandas as pd
import numpy as np

data = [
    ("A", "x1@gmail.com", 100.0, 120.0),
    ("A", "x2@yahoo.com", 250.0, 200.0),
    ("A", "x3@gmail.com", 300.0, 150.0),
    ("B", "y1@gmail.com", 180.0, 220.0),
    ("B", "y2@outlook.com", 500.0, 400.0),
    ("B", None,            50.0,  20.0),
]

df = pd.DataFrame(data, columns = ["group_key", "email", "amount", "amount2"])
df = df.groupby('group_key').agg(
    cnt = ('group_key',lambda x: x[df.loc[x.index,'amount']>df.loc[x.index,'amount2']].shape[0])
).reset_index()
print(df)