import pandas as pd


def calcular_kpis_hospitalarios(df: pd.DataFrame) -> dict:

    # Ocupación promedio del hospital
    ocupacion_promedio_pct = (
        df["camas_ocupadas"].sum()
        / df["camas_totales"].sum()
    ) * 100

    # Costo operativo total
    costo_total = df["costo_operativo_dia"].sum()

    # Camas libres
    camas_libres = (
        df["camas_totales"].sum()
        - df["camas_ocupadas"].sum()
    )

    # Estado de alerta
    if ocupacion_promedio_pct >= 85:
        estado_alerta = "CRÍTICO (Saturación)"
    else:
        estado_alerta = "Normal (Capacidad Estable)"

    # Devolver los resultados
    return {
        "ocupacion_promedio_pct": ocupacion_promedio_pct,
        "costo_total": costo_total,
        "camas_libres": camas_libres,
        "estado_alerta": estado_alerta
    }