

import streamlit as st
import pandas as pd

from datos_hospital import hospitales
from componente_metricas import calcular_kpis_hospitalarios

# 1. CREAR DATAFRAME

df = pd.DataFrame(hospitales)

# 2. CALCULAR KPI

kpis = calcular_kpis_hospitalarios(df)

# 3. TÍTULO

st.title("🏥 Dashboard Hospitalario")

st.write("Sistema de análisis de ocupación hospitalaria")

# 4. MOSTRAR LOS 4 KPI

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Ocupación promedio",
    f"{kpis['ocupacion_promedio_pct']:.1f}%"
)

col2.metric(
    "Costo total",
    f"${kpis['costo_total']:,.0f}"
)

col3.metric(
    "Camas libres",
    kpis["camas_libres"]
)

col4.metric(
    "Estado",
    kpis["estado_alerta"]
)

# 5. TABLA DE HOSPITALES

st.subheader("Datos de los hospitales")

st.write(df)
st.dataframe(df)
st.write(df.columns.tolist())
# st.bar_chart(df)

# 6. GRÁFICA DE CAMAS

st.subheader("Camas por hospital")

grafica = df.set_index("nombre")[[
    "camas_totales",
    "camas_ocupadas"
]]

st.bar_chart(grafica)
st.subheader("Descargar datos en Excel")

excel_file = "datos_hospitalarios.xlsx"

df.to_excel(excel_file, index=False)

with open(excel_file, "rb") as archivo:
    st.download_button(
        label="📥 Descargar Excel",
        data=archivo,
        file_name=excel_file,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
st.subheader("Camas ocupadas por hospital")
st.bar_chart(df[["nombre", "camas_ocupadas"]])

st.subheader("Costos operativos por hospital")
st.bar_chart(df[["nombre", "costo_operativo_dia"]])

# st.bar_chart(df[["hospital", "camas_ocupadas"]])

st.write(df.columns)

