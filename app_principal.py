import pandas as pd

from datos_hospital import hospitales
from componente_metricas import calcular_kpis_hospitalarios


# ==========================================
# 1. CREAR DATAFRAME
# ==========================================

df = pd.DataFrame(hospitales)


# ==========================================
# 2. CALCULAR LOS KPI
# ==========================================

kpis = calcular_kpis_hospitalarios(df)


# ==========================================
# 3. MOSTRAR LOS DATOS
# ==========================================

print("DATOS DEL HOSPITAL")
print("------------------")
print(df)


# ==========================================
# 4. MOSTRAR LOS RESULTADOS
# ==========================================

print()
print("KPI HOSPITALARIOS")
print("-----------------")

print("Ocupación promedio:",
      kpis["ocupacion_promedio_pct"])

print("Costo total:",
      kpis["costo_total"])

print("Camas libres:",
      kpis["camas_libres"])

print("Estado de alerta:",
      kpis["estado_alerta"])