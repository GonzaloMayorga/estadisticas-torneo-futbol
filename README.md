# Estadísticas de Resultados Deportivos

## Descripción

Proyecto desarrollado para el Trabajo Práctico de Gestión Colaborativa, Control de Versiones y Organización Empresarial.

El objetivo es analizar resultados de un torneo deportivo simulado, calcular estadísticas básicas y generar archivos de salida reproducibles mediante Python.

## Alumno

Gonzalo Gabriel Mayorga

## Modalidad

Trabajo individual, simulando los roles P1, P2 y P3 propuestos por la consigna.

## Escenario elegido

Estadísticas de Resultados Deportivos.

## Estructura del repositorio

- `datos/`: contiene el archivo `partidos.csv`.
- `scripts/`: contiene el script `analisis_resultados.py`.
- `resultados/`: contiene la tabla de posiciones, el resumen del torneo y el gráfico generado.
- `.gitignore`: evita subir archivos innecesarios.
- `README.md`: documentación del proyecto.

## Dataset

El dataset utilizado es simulado y contiene resultados de partidos de fútbol. Las columnas son:

- `fecha`
- `equipo_local`
- `equipo_visitante`
- `goles_local`
- `goles_visitante`

## Ejecución

Desde Google Colab o una terminal con Python instalado:

```bash
python scripts/analisis_resultados.py
```

El script genera los siguientes archivos:

```bash
resultados/tabla_posiciones.csv
resultados/resumen_torneo.txt
resultados/grafico_puntos_por_equipo.png
```
