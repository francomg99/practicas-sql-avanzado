import pandas as pd
import matplotlib.pyplot as plt

df_clientes = pd.read_csv('clientes.csv')
df_pedidos = pd.read_csv('pedidos.csv')

df_clientes['pais'] = df_clientes['pais'].str.strip().str.lower()

# FILTRAMOS
df_pedidos = df_pedidos[df_pedidos['estado'] == 'Entregado']
df_pedidos['ingreso_total'] = df_pedidos['cantidad'] * df_pedidos['precio']

# UNIMOS Y MODIFICACAMOS NAN
pedidos_entregados = pd.merge(left=df_clientes, right=df_pedidos, how='right', left_on='id_cliente', right_on='cod_cliente')
pedidos_entregados['nombre'] = pedidos_entregados['nombre'].fillna('Invitado')
pedidos_entregados['pais'] = pedidos_entregados['pais'].fillna('Invitado')

# AGRUPAMOS
resumen = pedidos_entregados.groupby('pais').agg({
    'ingreso_total': ['sum']
})

resumen.columns = [f'{col[0]}_{col[1]}'for col in resumen.columns]
resumen = resumen.reset_index()

# VISUALIZAMOS
colors = ['red', 'blue', 'orange', 'yellow', 'green', 'purple']
resumen.sort_values(
    'ingreso_total_sum', ascending=False).plot(
        kind='bar', 
        x='pais', 
        y='ingreso_total_sum',
        color=colors,
        grid=True,
        rot=45
        )
    
plt.title('Ingreso por Pais')
plt.xlabel('País')
plt.ylabel('Ingreso Total')
plt.show()

# EXPORTAMOS
resumen.to_excel('Reporte_final.xlsx', index=False, sheet_name='Ingreso por pais')


print(resumen)
