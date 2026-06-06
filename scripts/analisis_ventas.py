import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Leer CSV
df = pd.read_csv(BASE_DIR / "datos" / "sales_sample_2024.csv")

# Convertir fecha
df["sales_date"] = pd.to_datetime(df["sales_date"])

# Ventas totales del año
ventas_totales = df["sales_amount"].sum()

# Día con mayor venta
mayor_venta = df.loc[df["sales_amount"].idxmax()]

# Ventas por mes
ventas_mes = (
    df.groupby(df["sales_date"].dt.month)["sales_amount"]
    .sum()
)

print("=" * 40)
print("VENTAS TOTALES:", ventas_totales)
print("=" * 40)
print("DÍA CON MAYOR VENTA")
print("Fecha:", mayor_venta["sales_date"].date())
print("Monto:", mayor_venta["sales_amount"])
print("=" * 40)

# Gráfico
plt.figure(figsize=(10, 5))
ventas_mes.plot(marker="o")
plt.title("Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Monto Vendido")
plt.grid(True)

plt.savefig(BASE_DIR / "resultados" / "grafico_ventas.png")
plt.show()

print("Gráfico guardado en resultados/grafico_ventas.png")