# Requisitos del sistema

## Alcance

El Sistema de Gestión de Órdenes de Trabajo para Taller Automotriz busca organizar la información operativa de un taller mediante una fuente única para clientes, vehículos, órdenes, diagnósticos, repuestos, servicios, costos e historial.

## Requisitos funcionales

### RF-01 - Registro de clientes
El sistema debe permitir registrar, consultar y actualizar clientes con nombre, teléfono, correo y dirección.

### RF-02 - Registro de vehículos
El sistema debe permitir registrar vehículos asociados a un cliente, incluyendo marca, modelo, año, placa, VIN y kilometraje.

### RF-03 - Gestión de órdenes de trabajo
El sistema debe permitir crear y actualizar órdenes asociadas a un cliente y un vehículo, asignar un identificador único y controlar su estado.

Estados previstos:

`Recepción -> Diagnóstico -> Esperando aprobación -> En reparación -> Terminado -> Entregado`

### RF-04 - Registro de diagnóstico
El sistema debe permitir registrar síntomas observados, diagnóstico técnico, reparaciones recomendadas y observaciones para una orden existente.

### RF-05 - Repuestos, servicios, mano de obra y costos
El sistema debe permitir registrar conceptos de costo, cantidades y precios, y calcular subtotales y total de la orden.

### RF-06 - Historial de servicios
El sistema debe permitir consultar cronológicamente las órdenes anteriores de un vehículo utilizando placa o VIN.

## Historias de usuario principales

- **HU-01:** Como recepcionista, quiero registrar al cliente y su vehículo para disponer de la información necesaria al crear una orden.
- **HU-02:** Como recepcionista, quiero crear y actualizar una orden de trabajo para dar seguimiento al vehículo desde la recepción hasta la entrega.
- **HU-03:** Como técnico, quiero registrar el diagnóstico y las reparaciones recomendadas para dejar documentada la falla del vehículo.
- **HU-04:** Como encargado del taller, quiero registrar repuestos, servicios y mano de obra para conocer el costo total de la reparación.
- **HU-05:** Como recepcionista o técnico, quiero consultar el historial de un vehículo para conocer reparaciones anteriores.

## Requisitos no funcionales considerados

- Integridad y consistencia de los datos.
- Separación de responsabilidades entre interfaz, lógica y persistencia.
- Validaciones para campos obligatorios y datos duplicados.
- Facilidad de mantenimiento y evolución del sistema.
- Trazabilidad entre requisitos, Issues, cambios y pruebas.
