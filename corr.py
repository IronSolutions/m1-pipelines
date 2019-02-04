import pandas as pd

df = pd.read_csv('../vehicles/vehicles.csv')

print(df.corr())