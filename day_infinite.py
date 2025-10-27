import pandas as pd
from datetime import datetime
dates = pd.date_range(start="2025-01-01", end="2025-01-10")
df = pd.DataFrame(dates, columns=["datetime"])

start = '04/01/2025'
end = '08/01/2025'
start = datetime.strptime(start,'%d/%m/%Y').strftime('%Y-%m-%d')
end = datetime.strptime(end,'%d/%m/%Y').strftime('%Y-%m-%d')

df = df[(df['datetime']>start) & (df['datetime']<end)]
print(df)