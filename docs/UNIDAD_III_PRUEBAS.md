# Unidad III — Verificación y validación del componente RF-03 / HU-02

Línea base: a159ede74c400fcb36ff54f88ac8e65906d7cad6. Patrón State, lógica de negocio.

## Evidencia de ejecución local (24/11/2026)
Entorno: Windows PowerShell, Python 3.14.4, unittest de la biblioteca estándar.
Resultados registrados por el participante en terminal:

| Ejecución | Casos | Fallos en subpruebas | Errores en subpruebas | Tiempo |
|---|---:|---:|---:|---:|
| Regresión original | 9/9 aprobados | 0 | 0 | 0.004 s |
| Cinco casos nuevos sobre línea base | 1/5 aprobado | 4 | 8 | 0.042 s |
| Validación final | 14/14 aprobados | 0 | 0 | 0.015 s |

## Trazabilidad y correcciones
| Caso / criterio | Comportamiento esperado | No conformidad y corrección |
|---|---|---|
| CP-01 / CA-01 | Identificadores de texto no vacíos | NC-01: 6 errores AttributeError; comprobar tipo y contenido |
| CP-02 / CA-02 | Diagnóstico de texto no vacío | NC-02: 2 errores AttributeError; comprobar tipo y contenido |
| CP-03 / CA-03 | Aprobación estrictamente True | NC-03: 2 fallos; comparación booleana estricta |
| CP-04 / CA-04 | Reparación registrada estrictamente True | NC-04: 2 fallos; comparación booleana estricta |
| CP-05 / CA-05 | Flujo completo, historial y estado final | Aprobado antes y después |

Correcciones: [commit 6fe1e35](../commit/6fe1e35c6619b52616995c07a81b85e152a4b661).
Código: [orden_estado.py](../implementacion/orden_estado.py).
Pruebas: [Unidad III](../implementacion/tests/test_unidad3.py), [regresión](../implementacion/tests/test_orden_estado.py).

## Reproducción desde la raíz (PowerShell)
```powershell
$env:PYTHONPATH = (Resolve-Path ./implementacion).Path
python --version
python -m unittest discover -s implementacion/tests -v
```

Las pruebas comprueban integración interna del patrón State, no integración con API, interfaz ni base de datos. Los tiempos corresponden a la ejecución local del participante; no son mediciones de CI. Los cinco casos son operaciones del componente, no una confirmación de cinco casos UML independientes. Las capturas de terminal se adjuntan al informe académico.
