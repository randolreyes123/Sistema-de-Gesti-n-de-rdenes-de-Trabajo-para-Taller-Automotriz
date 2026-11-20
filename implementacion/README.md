# Ingeniería de Software II – Semana II: Patrón State

Prototipo ejecutable del control de estados de órdenes de trabajo del proyecto de taller automotriz. Corresponde al requisito RF-03 y a la historia HU-02 del repositorio académico. Es una **adaptación aislada**, no una integración realizada con la API o base de datos; ese producto aún se encuentra documentado como línea base 0.1.

## Ejecución

Python 3.10+ sin dependencias externas.

```bash
cd implementacion
python -m unittest discover -s tests -v
```

## Diseño

- `OrdenTrabajo`: contexto y entidad que delega la transición.
- `EstadoOrden`: interfaz de estados.
- `Recepcion`, `Diagnostico`, `EsperandoAprobacion`, `EnReparacion`, `Terminado`, `Entregado`: comportamiento por estado.
- `ESTADOS`: registro de objetos de estado.
- `TransicionInvalida`: error de reglas de negocio.

La progresión es deliberadamente lineal y reproduce lo documentado en el repositorio. No cubre cancelaciones, devolución a diagnóstico, autorizaciones por roles ni persistencia. Las aprobaciones están modeladas como booleanos para demostrar la guarda, pero una solución real requerirá autorización y auditoría.
