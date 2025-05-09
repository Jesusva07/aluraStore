"""
Análisis de eficiencia para Alura Store
Determina qué tienda recomendar para vender basado en métricas de desempeño.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda1 = pd.read_csv(url)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

print(tienda1.head())

print("Columnas en Tienda 1:", tienda1.columns.tolist())

ingreso_tienda1 = tienda1['Precio'].sum()
ingreso_tienda2 = tienda2['Precio'].sum()
ingreso_tienda3 = tienda3['Precio'].sum()
ingreso_tienda4 = tienda4['Precio'].sum()

print("\n--- Ingresos Totales ---")
print(f"Tienda 1: ${ingreso_tienda1:,.2f}")
print(f"Tienda 2: ${ingreso_tienda2:,.2f}")
print(f"Tienda 3: ${ingreso_tienda3:,.2f}")
print(f"Tienda 4: ${ingreso_tienda4:,.2f}")

tiendas = {
    "Tienda 1": tienda1,
    "Tienda 2": tienda2,
    "Tienda 3": tienda3,
    "Tienda 4": tienda4
}

for nombre, df in tiendas.items():
    print(f"\n🔍 {nombre}: Productos vendidos por categoría")
    # Agrupar por categoría y sumar la cantidad vendida
    ventas_por_categoria = df.groupby('Categoría del Producto')['Cantidad de cuotas'].sum().sort_values(ascending=False)
    print(ventas_por_categoria)

# Calcular calificación promedio por tienda
print("\n⭐ Calificación promedio por tienda (1-5):")
for nombre, df in tiendas.items():
    promedio = df['Calificación'].mean().round(2)  # Redondeo a 2 decimales
    print(f"{nombre}: {promedio}/5")

for nombre, df in tiendas.items():
    # 1. Agrupar por producto y sumar cantidades vendidas
    ventas_por_producto = df.groupby('Producto')['Cantidad de cuotas'].sum().sort_values(ascending=False)
    
    # 2. Identificar top y peor producto
    top_producto = ventas_por_producto.idxmax()
    top_ventas = ventas_por_producto.max()
    peor_producto = ventas_por_producto.idxmin()
    peor_ventas = ventas_por_producto.min()
    
    print(f"\n📌 {nombre}:")
    print(f"   🏆 TOP: '{top_producto}' ({top_ventas} unidades)")
    print(f"   🔻 PEOR: '{peor_producto}' ({peor_ventas} unidades)")

    # 3. Gráfico de los 10 productos más vendidos
    ventas_por_producto.head(10).plot(
        kind='barh', 
        color='#2ecc71',
        title=f'Top 10 Productos - {nombre}'
    )
    plt.xlabel('Unidades Vendidas')
    plt.tight_layout()
    plt.show()

print("\n🚚 Costo promedio de envío por tienda:")
for nombre, df in tiendas.items():
    costo_promedio = df['Costo de envío'].mean().round(2)  # Redondeado a 2 decimales
    print(f"  {nombre}: ${costo_promedio}")

# Opcional: Gráfico de costos
costos = [df['Costo de envío'].mean() for df in tiendas.values()]
nombres = list(tiendas.keys())

plt.bar(nombres, costos, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'])
plt.title('Costo Promedio de Envío por Tienda')
plt.ylabel('Costo ($)')
plt.xlabel('Tienda')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

import seaborn as sns  # Si no lo tienes: pip install seaborn

# Preparar datos
datos_envios = pd.concat([
    tienda1.assign(Tienda='Tienda 1'),
    tienda2.assign(Tienda='Tienda 2'),
    tienda3.assign(Tienda='Tienda 3'),
    tienda4.assign(Tienda='Tienda 4')
])


plt.figure(figsize=(10, 6))
sns.violinplot(x='Tienda', y='Costo de envío', data=datos_envios, palette='pastel')
plt.title('Distribución de Costos de Envío por Tienda')
plt.xlabel('Tienda')
plt.ylabel('Costo ($)')
plt.grid(axis='y', linestyle='--')
plt.show()

