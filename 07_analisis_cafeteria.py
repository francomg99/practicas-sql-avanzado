import pandas as pd

df = pd.read_csv('cafeteria.csv')

# 1. Convertir
df['fecha_limpia'] = pd.to_datetime(df['fecha_registro'])

# 2. Extraer
df['dia_semana'] = df['fecha_limpia'].dt.day_name()

# 3. Ordenar (Sobreescribimos la MISMA tabla 'df')
df = df.sort_values('fecha_limpia')

# 4. Calcular sobre la tabla que ya está ordenada
df['variacion_diaria'] = df['ganancia'] - df['ganancia'].shift(1)
