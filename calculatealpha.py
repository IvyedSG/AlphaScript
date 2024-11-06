import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Función para calcular el alfa de Cronbach
def cronbach_alpha(df):
    df_corr = df.corr()
    n = len(df.columns)
    return (n / (n - 1)) * (1 - (df_corr.values.diagonal().sum() / df_corr.values.sum()))

# Ruta del archivo Excel
file_path = 'C:/Users/pc1/Desktop/AlfaDeCronbachScript/karla.xlsx'

# Cargar el archivo Excel
data = pd.read_excel(file_path)

# Seleccionar las columnas correspondientes a las variables de interés
redes_sociales = data.iloc[:, 0:22]  # Primeras 24 columnas para redes sociales
rendimiento_academico = data.iloc[:, 22:]  # Columnas restantes para rendimiento académico

# Convertir las respuestas categóricas en valores numéricos
label_encoder = LabelEncoder()
redes_sociales_numeric = redes_sociales.apply(lambda col: label_encoder.fit_transform(col.astype(str)) + 1)
rendimiento_academico_numeric = rendimiento_academico.apply(lambda col: label_encoder.fit_transform(col.astype(str)) + 1)

# Calcular el alfa de Cronbach para cada variable
alpha_redes_sociales = cronbach_alpha(redes_sociales_numeric)
alpha_rendimiento_academico = cronbach_alpha(rendimiento_academico_numeric)

print(f"""
=======================================================
     Alfa de Cronbach para Redes Sociales: {alpha_redes_sociales}
     Alfa de Cronbach para Rendimiento Académico: {alpha_rendimiento_academico}
=======================================================
""")
