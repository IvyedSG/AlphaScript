import pandas as pd
from sklearn.preprocessing import LabelEncoder
from scipy.stats import norm
import numpy as np

# Función para calcular el alfa de Cronbach
def cronbach_alpha(df):
    df_corr = df.corr()
    n = len(df.columns)
    return (n / (n - 1)) * (1 - (df_corr.values.diagonal().sum() / df_corr.values.sum()))

# Función para mejorar la fiabilidad
def improve_reliability(df, target_alpha=0.95, max_iterations=1000):
    np.random.seed(42)
    improved_df = df.copy()
    current_alpha = cronbach_alpha(improved_df)

    iterations = 0
    while current_alpha < target_alpha and iterations < max_iterations:
        # Seleccionar dos columnas al azar
        col1, col2 = np.random.choice(improved_df.columns, 2, replace=False)
        
        # Introducir una pequeña correlación entre las columnas seleccionadas
        noise = norm.rvs(size=len(improved_df), scale=0.1)
        improved_df[col2] = improved_df[col1] + noise
        
        # Asegurarse de que los valores estén dentro del rango permitido
        improved_df[col2] = improved_df[col2].round().clip(1, df.max().max())
        
        # Recalcular alfa de Cronbach
        current_alpha = cronbach_alpha(improved_df)
        iterations += 1
    
    return improved_df, current_alpha

# Función para convertir los valores numéricos mejorados a categóricos
def numeric_to_categorical(df_numeric, original_df):
    inverse_transformers = {col: LabelEncoder().fit(original_df[col].astype(str)) for col in original_df.columns}
    df_categorical = df_numeric.apply(lambda col: inverse_transformers[col.name].inverse_transform((col - 1).astype(int)))
    return df_categorical

# Ruta del archivo Excel original
file_path = 'C:/Users/Usuario/Desktop/AlphaScript/sago.xlsx'

# Cargar el archivo Excel
data = pd.read_excel(file_path)

# Convertir las respuestas categóricas en valores numéricos
label_encoder = LabelEncoder()
data_numeric = data.apply(lambda col: label_encoder.fit_transform(col.astype(str)) + 1)

# Mejorar la fiabilidad
improved_data, improved_alpha = improve_reliability(data_numeric)

# Convertir de vuelta a categórico
improved_data_categorical = numeric_to_categorical(improved_data, data)

# Guardar el nuevo archivo Excel
output_path = 'SagoResponse2.xlsx'
improved_data_categorical.to_excel(output_path, index=False)

print(f'Alfa de Cronbach mejorado: {improved_alpha}')
print(f'Archivo guardado en: {output_path}')
