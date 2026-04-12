import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ventas_q1.csv')

filtrado = df[(df['pais'].isin(['Argentina','Chile'])) & (df['unidades_vendidas']>0)].copy()
filtrado['ingreso_total'] = filtrado['unidades_vendidas']*filtrado['precio_unitario']

resumen = filtrado.groupby('pais').agg({
    'ingreso_total': ['sum'],
    'unidades_vendidas': ['max']
})

resumen.columns = [f'{col[0]}_{col[1]}' for col in resumen.columns]
resumen = resumen.reset_index()

colors = ['blue', 'orange']
resumen.sort_values('ingreso_total_sum', ascending = False).plot(kind='bar', x='pais', y='ingreso_total_sum', color=colors)

plt.title('Ingresos totales por país')
plt.xlabel('Pais')
plt.ylabel('Ingreso total')
plt.show()

resumen.to_excel('Ingreso_total_pais.xlsx', index=False, sheet_name='Resumen')
