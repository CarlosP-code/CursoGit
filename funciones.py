def calcular_kpis_hospitalarios(df):

    # ==========================================
    # 1. OCUPACIÓN PROMEDIO
    # ==========================================

    ocupacion_promedio = df["ocupacion_pct"].mean()


    # ==========================================
    # 2. CAMAS LIBRES
    # ==========================================

    camas_libres = df["camas_libres"].sum()


    # ==========================================
    # 3. OCUPACIÓN MÁXIMA
    # ==========================================

    ocupacion_maxima = df["ocupacion_pct"].max()


    # ==========================================
    # 4. ESTADO GENERAL
    # ==========================================

    if ocupacion_promedio >= 85:
        estado = "CRÍTICO (Saturación)"
    else:
        estado = "Normal (Capacidad Estable)"


    # ==========================================
    # 5. DEVOLVER LOS KPI
    # ==========================================

    return {
        "ocupacion_promedio": ocupacion_promedio,
        "camas_libres": camas_libres,
        "ocupacion_maxima": ocupacion_maxima,
        "estado": estado
    }