import pandas as pd
file = r"C:\User\Kornelius\Downloads\sales_datasheet1.csv"
df = pd.read_csv(file, sep=";")
print(df)
