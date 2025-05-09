# 🛒 Análisis de Eficiencia - Alura Store

Este proyecto realiza un **análisis exploratorio de datos (EDA)** sobre el desempeño de cuatro tiendas de la empresa ficticia *Alura Store*, con el fin de determinar cuál tienda tiene mejor rendimiento y cuál debería considerarse para cierre o reestructuración.

---

## 📊 Objetivo del Proyecto

Comparar el desempeño de las tiendas en cuanto a:
- **Ingresos totales**
- **Cantidad de productos vendidos por categoría**
- **Calificación promedio de los productos**
- **Costo promedio de envío**
- **Identificación de productos top y con bajo desempeño**
- **Visualización de métricas clave para facilitar la toma de decisiones**

---

## 🧰 Tecnologías y Librerías Usadas

- Python 3.x
- `pandas`
- `matplotlib`
- `seaborn`
- `numpy`

---

## 📂 Estructura del Código

- **Carga de Datos:** Se descargan y procesan los CSV de cada tienda desde URLs públicas de GitHub.
- **Análisis Numérico:**
  - Suma de ingresos (`Precio`)
  - Agrupamiento por categorías de producto
  - Calificaciones promedio
  - Costos de envío promedio
- **Visualización:**
  - Gráficos de barras para productos más vendidos
  - Gráfico de costos promedio por tienda
  - Gráfico violin para distribución de costos de envío

---

## 📈 Resultados Generados

- Ranking de tiendas por ingreso total
- Gráfico de los 10 productos más vendidos por tienda
- Categorización de productos vendidos por tienda
- Costos de envío comparados gráficamente
- Evaluación de la experiencia del cliente mediante calificaciones

---

## 🧠 Recomendación

Con base en las métricas generadas, el análisis permite **recomendar cuál tienda tiene un mejor desempeño** y cuál presenta áreas críticas de mejora, considerando tanto eficiencia financiera como satisfacción del cliente.

---

## 🚀 Cómo Ejecutarlo

1. Asegúrate de tener Python 3.9 o superior.
2. Instala las dependencias necesarias:
Bibliotecas: pandas, matplotlib, seaborn  y numpy

## 📁 Archivos Clave
aluraStore.py: Código principal de análisis y visualización.

CSVs de tiendas: Se cargan desde URLs públicas (no se incluyen en el repositorio).

✍️ Autor
Jesús David Valencia León
Estudiante de ONE-Alura Analis de datos
