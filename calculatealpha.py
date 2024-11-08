import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Función para calcular el alfa de Cronbach
def cronbach_alpha(df):
    df_corr = df.corr()
    n = len(df.columns)
    return (n / (n - 1)) * (1 - (df_corr.values.diagonal().sum() / df_corr.values.sum()))

# Ruta del archivo Excel
file_path = 'C:/Users/Usuario/Desktop/AlphaScript/SagoResponse2.xlsx'

# Cargar el archivo Excel
data = pd.read_excel(file_path)

# Seleccionar las columnas correspo1ndientes a las variables de interés
tics = data.iloc[:, 0:10]  # Primeras 24 columnas para redes sociales
alpha_abp = data.iloc[:,10:]  # Columnas restantes para rendimiento académico

# Convertir las respuestas categóricas en valores numéricos
label_encoder = LabelEncoder()
habitos_estudio = tics.apply(lambda col: label_encoder.fit_transform(col.astype(str)) + 1)
rendimiento_aca = alpha_abp.apply(lambda col: label_encoder.fit_transform(col.astype(str)) + 1)

# Calcular el alfa de Cronbach para cada variable
habitos_estudios = cronbach_alpha(habitos_estudio)
rendimiento_acas = cronbach_alpha(rendimiento_aca)

print(f"""
=======================================================
     Alfa de Cronbach para habitos_estudio: {habitos_estudios}
     Alfa de Cronbach para rendimiento_aca: {rendimiento_acas}
=======================================================
""")
