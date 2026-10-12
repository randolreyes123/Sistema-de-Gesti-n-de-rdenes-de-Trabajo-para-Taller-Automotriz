# Seguimiento del proyecto

## Método de trabajo

El proyecto se organizó con un enfoque ágil basado en Kanban utilizando GitHub Projects y GitHub Issues.

Estados utilizados:

`Backlog | Por hacer | En progreso | En revisión | Finalizado`

## Estado documentado de las tareas

| Issue | Tarea | Prioridad | Estado documentado |
|---|---|---|---|
| #1 | Diseñar registro de clientes | Alta | Finalizado |
| #2 | Diseñar registro de vehículos | Alta | En revisión |
| #3 | Crear módulo de órdenes de trabajo | Alta | En progreso |
| #4 | Crear módulo de diagnóstico | Media | En progreso |
| #5 | Registrar repuestos y costos | Media | En progreso |
| #6 | Crear historial de servicios | Media | Backlog |
| #7 | Definición de arquitectura inicial | Alta | Finalizado |
| #8 | Diseñar modelo entidad-relación de la base de datos | Alta | En revisión |
| #9 | Implementar validaciones de datos del sistema | Alta | Por hacer |
| #10 | Realizar pruebas funcionales e integración | Media | Por hacer |

## Issues seleccionados para el cierre técnico

### Issue #3 - Crear módulo de órdenes de trabajo
Representa el núcleo funcional del sistema. Su avance condiciona el diagnóstico, los costos y el historial.

### Issue #6 - Crear historial de servicios
Representa una mejora funcional pendiente y depende de que las órdenes anteriores estén correctamente almacenadas y relacionadas con cada vehículo.

### Issue #9 - Implementar validaciones de datos del sistema
Representa un riesgo técnico importante: sin validaciones pueden almacenarse datos incompletos, duplicados o inconsistentes.

### Issue #10 - Realizar pruebas funcionales e integración
Representa una tarea necesaria para comprobar que los módulos funcionen correctamente de forma individual y en conjunto.

## Observación

El tablero refleja un proyecto en fase inicial de ingeniería y desarrollo. Por tanto, no todas las tareas aparecen como finalizadas; los estados se conservan según el avance real documentado durante la asignatura.
