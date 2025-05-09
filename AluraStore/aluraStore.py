"""
Análisis de eficiencia para Alura Store
Determina qué tienda recomendar para vender basado en métricas de desempeño.
"""

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

