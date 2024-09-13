import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv("_annotations.csv")

# Ordenar el DataFrame por el campo deseado en orden ascendente
df_sorted = df.sort_values(by="filename", ascending=True)

print(df_sorted.head())
df_sorted = df_sorted.head(2001)
# Guardar el DataFrame ordenado en un nuevo archivo CSV
df_sorted.to_csv("balls.csv", index=False)