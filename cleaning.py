import pandas as pd

# cargar dataset
data = pd.read_csv("dirty_data.csv")

print("Original dataset:")
print(data)

# eliminar duplicados
data = data.drop_duplicates()

# eliminar filas con datos faltantes
data = data.dropna()

print("\nCleaned dataset:")
print(data)

# guardar dataset limpio
data.to_csv("cleaned_data.csv", index=False)

print("\nCleaned dataset saved as cleaned_data.csv")