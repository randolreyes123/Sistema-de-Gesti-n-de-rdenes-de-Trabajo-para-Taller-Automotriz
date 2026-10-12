# Modelos UML

Durante el análisis del sistema se trabajaron modelos UML para representar el sistema desde distintas perspectivas.

## Modelos elaborados

- Diagrama de casos de uso.
- Diagrama de clases.
- Diagrama de secuencia.
- Diagrama de colaboración.
- Diagrama de actividades.
- Diagrama de componentes para representar la arquitectura por capas.

## Vista funcional resumida

Actores principales:

- Recepcionista.
- Técnico.
- Encargado del taller.

Casos de uso principales:

- Registrar cliente.
- Registrar vehículo.
- Crear y actualizar orden de trabajo.
- Registrar diagnóstico.
- Registrar repuestos, servicios y mano de obra.
- Calcular costos.
- Consultar historial del vehículo.

## Vista estructural resumida

Entidades principales:

- Cliente.
- Vehículo.
- Orden de trabajo.
- Diagnóstico.
- Servicio.
- Repuesto.
- Detalle de orden.

La orden de trabajo funciona como elemento central del modelo, relacionando al cliente y al vehículo con el diagnóstico, los trabajos realizados y los costos.

## Vista de comportamiento

El flujo principal de una orden se definió como:

`Recepción -> Diagnóstico -> Esperando aprobación -> En reparación -> Terminado -> Entregado`

Los diagramas originales fueron elaborados en Visual Paradigm Online como parte de las evidencias de la asignatura.
