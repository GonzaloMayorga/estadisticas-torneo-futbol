import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATOS_PATH = BASE_DIR / "datos" / "partidos.csv"
RESULTADOS_DIR = BASE_DIR / "resultados"

RESULTADOS_DIR.mkdir(exist_ok=True)

# Cargar dataset
partidos = pd.read_csv(DATOS_PATH)

# Obtener listado único de equipos
equipos = sorted(
    set(partidos["equipo_local"]).union(set(partidos["equipo_visitante"]))
)

# Inicializar tabla de posiciones
tabla = {
    equipo: {
        "PJ": 0,
        "PG": 0,
        "PE": 0,
        "PP": 0,
        "GF": 0,
        "GC": 0,
        "DG": 0,
        "PTS": 0,
    }
    for equipo in equipos
}

# Procesar cada partido para calcular estadísticas por equipo
for _, partido in partidos.iterrows():
    local = partido["equipo_local"]
    visitante = partido["equipo_visitante"]
    goles_local = partido["goles_local"]
    goles_visitante = partido["goles_visitante"]

    # Registrar partidos jugados
    tabla[local]["PJ"] += 1
    tabla[visitante]["PJ"] += 1

    # Registrar goles a favor y en contra
    tabla[local]["GF"] += goles_local
    tabla[local]["GC"] += goles_visitante
    tabla[visitante]["GF"] += goles_visitante
    tabla[visitante]["GC"] += goles_local

    # Asignar puntos según el resultado del partido
    if goles_local > goles_visitante:
        tabla[local]["PG"] += 1
        tabla[visitante]["PP"] += 1
        tabla[local]["PTS"] += 3
    elif goles_local < goles_visitante:
        tabla[visitante]["PG"] += 1
        tabla[local]["PP"] += 1
        tabla[visitante]["PTS"] += 3
    else:
        tabla[local]["PE"] += 1
        tabla[visitante]["PE"] += 1
        tabla[local]["PTS"] += 1
        tabla[visitante]["PTS"] += 1

# Convertir la tabla calculada a DataFrame
tabla_df = pd.DataFrame.from_dict(tabla, orient="index")
tabla_df["DG"] = tabla_df["GF"] - tabla_df["GC"]

# Ordenar por puntos, diferencia de gol y goles a favor
tabla_df = tabla_df.sort_values(
    by=["PTS", "DG", "GF"],
    ascending=False
).reset_index()

tabla_df = tabla_df.rename(columns={"index": "Equipo"})

# Calcular métricas generales del torneo
total_goles = partidos["goles_local"].sum() + partidos["goles_visitante"].sum()
cantidad_partidos = len(partidos)
promedio_goles = total_goles / cantidad_partidos

# Guardar tabla de posiciones
tabla_df.to_csv(RESULTADOS_DIR / "tabla_posiciones.csv", index=False)

# Guardar resumen general
with open(RESULTADOS_DIR / "resumen_torneo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Resumen del torneo\n")
    archivo.write("==================\n\n")
    archivo.write(f"Cantidad de partidos analizados: {cantidad_partidos}\n")
    archivo.write(f"Total de goles convertidos: {total_goles}\n")
    archivo.write(f"Promedio de goles por partido: {promedio_goles:.2f}\n")
    archivo.write(f"Equipo puntero: {tabla_df.iloc[0]['Equipo']}\n")

# Generar gráfico comparativo de puntos por equipo
plt.figure(figsize=(10, 6))
plt.bar(tabla_df["Equipo"], tabla_df["PTS"])
plt.title("Puntos por equipo")
plt.xlabel("Equipo")
plt.ylabel("Puntos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(RESULTADOS_DIR / "grafico_puntos_por_equipo.png")
plt.close()

print("Análisis finalizado correctamente.")
print()
print(tabla_df)
print()
print(f"Promedio de goles por partido: {promedio_goles:.2f}")
