import pandas as pd

df_gimnasio = pd.read_csv('gimnasio.csv')

reporte = pd.pivot_table(
    data = df_gimnasio,
    values = 'asistentes',
    index = 'ciudad',
    columns = 'tipo_clase',
    aggfunc = 'sum',
    fill_value= 0,
    margins= True
)

print(reporte)
