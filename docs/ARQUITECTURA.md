# Arquitectura del sistema

## Estilo arquitectónico

Se seleccionó una **arquitectura por capas** para distribuir responsabilidades y evitar que la interfaz, las reglas de negocio y la persistencia queden mezcladas.

## Capas principales

### 1. Presentación / Frontend
Responsable de formularios, consultas, navegación y visualización de clientes, vehículos, órdenes, diagnósticos, repuestos, costos e historial.

### 2. Servicios / API
Expone las operaciones del sistema, recibe las solicitudes del frontend y coordina su paso hacia la lógica de negocio.

### 3. Lógica de negocio
Contiene las reglas principales del sistema: validaciones, control de estados de las órdenes, relación cliente-vehículo-orden, cálculo de costos y restricciones funcionales.

### 4. Acceso a datos
Centraliza las operaciones de consulta, inserción y actualización de datos.

### 5. Base de datos
Almacena de forma persistente clientes, vehículos, órdenes de trabajo, diagnósticos, servicios, repuestos y costos.

## Frontend y backend

El **frontend** se limita a la interacción con el usuario y a validaciones básicas de presentación. El **backend** concentra las reglas de negocio, las validaciones obligatorias, el cálculo de costos y el acceso a datos.

La interfaz no debe comunicarse directamente con la base de datos.

## Comunicación

Frontend y backend se comunicarían mediante una API, utilizando solicitudes HTTP/REST y estructuras de datos como JSON. Este enfoque facilita que la interfaz pueda cambiar sin modificar directamente la lógica y la persistencia.

## Principio de diseño aplicado

**Separación de responsabilidades.** Cada capa tiene una función definida y depende lo menos posible de los detalles internos de otras capas.

## Riesgo arquitectónico identificado

Una división incorrecta de responsabilidades puede generar dependencias innecesarias entre capas. Por esa razón, las reglas de negocio no deben quedar implementadas únicamente en la interfaz ni las consultas a la base de datos dispersas en distintos módulos.
