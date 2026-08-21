print("Hola amiguis")

nombre = "Carlos"
print(nombre)

camas_ocupadas = 240
camas_totales = 300
ocupacion = (camas_ocupadas / camas_totales) * 100
print(ocupacion)

camas_libres = camas_totales - camas_ocupadas
print(camas_libres)

print(type(nombre))
print(type(camas_ocupadas))
print(type(ocupacion))

def saludar():
    print("Hola desde una función")

saludar()


def calcular_ocupacion(ocupadas, totales):
    ocupacion = (ocupadas / totales) * 100
    return ocupacion

resultado = calcular_ocupacion(240, 300)
print(resultado)

persona = {
    "nombre": "Carlos",
    "edad": 66,
    "ciudad": "Vitoria-Gasteiz"
}
print(persona)

persona = {
    "nombre": "Carlos",
    "edad": 66,
    "ciudad": "Vitoria-Gasteiz"
}
print(persona)

print(persona["nombre"])

print(persona["edad"])
print(persona["ciudad"])

print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])


def calcular_datos_hospital(ocupadas, totales):
    ocupacion = (ocupadas / totales) * 100
    camas_libres = totales - ocupadas

    resultados = {
        "ocupacion": ocupacion,
        "camas_libres": camas_libres
    }

    return resultados

datos = calcular_datos_hospital(240, 300)

print(datos)

print(datos["ocupacion"])
print(datos["camas_libres"])

resultados = {
    "ocupacion": 80.0,
    "camas_libres": 60
}


import pandas as pd
datos_hospital = {
    "hospital": ["Hospital A", "Hospital B", "Hospital C"],
    "camas_ocupadas": [240, 180, 120],
    "camas_totales": [300, 250, 150],
    "costo_operativo_dia": [5000, 6000, 4000]
}

datos_hospital = {
    "hospital": ["Hospital A", "Hospital B", "Hospital C"],
    "camas_ocupadas": [240, 180, 120],
    "camas_totales": [300, 250, 150],
    "costo_operativo_dia": [5000, 6000, 4000]
}

df = pd.DataFrame(datos_hospital)

print(df)
print(df["camas_ocupadas"])

print(df["camas_ocupadas"].sum())

df["camas_ocupadas"].sum()
df["camas_totales"]
print(df["camas_totales"].sum())

total_camas_ocupadas = df["camas_ocupadas"].sum()
total_camas_totales = df["camas_totales"].sum()

ocupacion_promedio_pct = (
    total_camas_ocupadas / total_camas_totales
) * 100

print(ocupacion_promedio_pct)

print(round(ocupacion_promedio_pct, 2))

costo_total = df["costo_operativo_dia"].sum()
print(costo_total)

camas_libres = total_camas_totales - total_camas_ocupadas
print(camas_libres)

if ocupacion_promedio_pct >= 85:
    estado_alerta = "CRÍTICO (Saturación)"
else:
    estado_alerta = "Normal (Capacidad Estable)"

print(estado_alerta)

def calcular_kpis_hospitalarios(df):

    total_camas_ocupadas = df["camas_ocupadas"].sum()

    total_camas_totales = df["camas_totales"].sum()

    ocupacion_promedio_pct = (
        total_camas_ocupadas / total_camas_totales
    ) * 100

    costo_total = df["costo_operativo_dia"].sum()

    camas_libres = total_camas_totales - total_camas_ocupadas

    if ocupacion_promedio_pct >= 85:
        estado_alerta = "CRÍTICO (Saturación)"
    else:
        estado_alerta = "Normal (Capacidad Estable)"

    resultados = {
        "ocupacion_promedio_pct": ocupacion_promedio_pct,
        "costo_total": costo_total,
        "camas_libres": camas_libres,
        "estado_alerta": estado_alerta
    }

    return resultados
kpis = calcular_kpis_hospitalarios(df)
print(kpis)
print(kpis["ocupacion_promedio_pct"])
print(kpis["costo_total"])
print(kpis["camas_libres"])
print(kpis["estado_alerta"])
print(kpis["ocupacion_promedio_pct"])
kpis["ocupacion_promedio_pct"]
kpis["costo_total"]
kpis["camas_libres"]
kpis["estado_alerta"]
print(round(ocupacion_promedio_pct, 2))

resultados = {
        "ocupacion_promedio_pct": round(ocupacion_promedio_pct, 2),
        "costo_total": costo_total,
        "camas_libres": camas_libres,
        "estado_alerta": estado_alerta
    }


def calcular_kpis_hospitalarios(df):

    total_camas_ocupadas = df["camas_ocupadas"].sum()

    total_camas_totales = df["camas_totales"].sum()

    ocupacion_promedio_pct = (
        total_camas_ocupadas / total_camas_totales
    ) * 100

    costo_total = df["costo_operativo_dia"].sum()

    camas_libres = total_camas_totales - total_camas_ocupadas
    resultados = {
        "ocupacion_promedio_pct": round(ocupacion_promedio_pct, 2),
        "costo_total": costo_total,
        "camas_libres": camas_libres,
        "estado_alerta": estado_alerta
    }

    return resultados

kpis = calcular_kpis_hospitalarios(df)
print(kpis)


 