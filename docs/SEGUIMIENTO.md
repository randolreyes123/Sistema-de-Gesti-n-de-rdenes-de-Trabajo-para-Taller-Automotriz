# Seguimiento del proyecto

## Método de trabajo

El proyecto se organizó con un enfoque ágil basado en Kanban utilizando GitHub Projects y GitHub Issues.

Para el cierre de la Semana VIII, los estados utilizados en el tablero son:

`Reserva | Listo | En curso | En revisión | Hecho`

## Estado actual del tablero - 13/10/2026

| Issue | Tarea | Prioridad | Estado actual |
|---|---|---|---|
| #1 | Diseñar registro de clientes | Alta | Hecho |
| #2 | Diseñar registro de vehículos | Alta | Listo |
| #3 | Crear módulo de órdenes de trabajo | Alta | Listo |
| #4 | Crear módulo de diagnóstico | Media | Reserva |
| #5 | Registrar repuestos y costos | Media | Reserva |
| #6 | Crear historial de servicios | Media | Reserva |
| #7 | Definición de arquitectura inicial | Alta | Hecho |
| #8 | Diseñar modelo entidad-relación de la base de datos | Alta | Reserva |
| #9 | Implementar validaciones de datos del sistema | Alta | Reserva |
| #10 | Realizar pruebas funcionales e integración | Media | Reserva |

## Trazabilidad con el seguimiento anterior

Los Issues conservan dentro de su descripción el estado que tenían documentado en la Semana VI. En la actualización de cierre se agregó un bloque superior con el **estado actual del tablero**, evitando perder el registro histórico del avance.

## Issues seleccionados para el cierre técnico

### Issue #3 - Crear módulo de órdenes de trabajo
Representa el núcleo funcional del sistema. Actualmente está **Listo**, por lo que es el candidato inmediato para pasar a **En curso** cuando comience la implementación. Su avance condiciona el diagnóstico, los costos y el historial.

### Issue #6 - Crear historial de servicios
Actualmente está en **Reserva**. Representa una mejora funcional pendiente y depende de que las órdenes anteriores estén correctamente almacenadas y relacionadas con cada vehículo.

### Issue #9 - Implementar validaciones de datos del sistema
Actualmente está en **Reserva**. Representa un riesgo técnico importante: sin validaciones pueden almacenarse datos incompletos, duplicados o inconsistentes.

### Issue #10 - Realizar pruebas funcionales e integración
Actualmente está en **Reserva**. Será necesaria para comprobar que los módulos funcionen correctamente de forma individual y en conjunto.

## Cierre

El tablero refleja un proyecto en fase inicial de ingeniería y desarrollo. Los elementos **Hecho** corresponden a trabajo de análisis y arquitectura ya cerrado; los elementos **Listo** están preparados para iniciar la siguiente etapa; y los elementos **Reserva** permanecen pendientes de priorización o dependencia técnica.
