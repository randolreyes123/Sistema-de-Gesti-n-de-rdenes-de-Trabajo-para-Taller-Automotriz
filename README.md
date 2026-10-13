# Sistema de Gestión de Órdenes de Trabajo para Taller Automotriz

Proyecto académico desarrollado para la asignatura **Ingeniería de Software I**. La propuesta busca centralizar y organizar la información que se genera en un taller automotriz desde la recepción del vehículo hasta su entrega al cliente.

## Problema que resuelve

En talleres pequeños y medianos es común que los datos de clientes, vehículos, diagnósticos, repuestos, costos y estados de reparación se encuentren dispersos entre libretas, mensajes y registros independientes. Esto aumenta el riesgo de pérdida de información, duplicidad de datos, errores de cálculo y poca trazabilidad del trabajo realizado.

## Objetivo

Diseñar la base de un sistema que permita registrar clientes y vehículos, crear y dar seguimiento a órdenes de trabajo, documentar diagnósticos, registrar servicios, repuestos y mano de obra, calcular costos y consultar el historial de mantenimiento de cada vehículo.

## Usuarios principales

- **Recepcionista:** registra clientes, vehículos y órdenes de trabajo.
- **Técnico:** documenta diagnósticos, observaciones y reparaciones recomendadas.
- **Encargado del taller:** consulta el estado del trabajo, costos e historial del vehículo.

## Funcionalidades principales

- Registro y consulta de clientes.
- Registro y consulta de vehículos.
- Creación y seguimiento de órdenes de trabajo.
- Registro de diagnósticos y reparaciones recomendadas.
- Registro de repuestos, servicios y mano de obra.
- Cálculo de costos de la orden.
- Consulta del historial de servicios por vehículo.
- Validación de datos y control de estados de la orden.

## Flujo principal de una orden

`Recepción -> Diagnóstico -> Esperando aprobación -> En reparación -> Terminado -> Entregado`

## Arquitectura seleccionada

Se definió una **arquitectura por capas** para separar responsabilidades y reducir el acoplamiento entre componentes.

1. **Presentación / Frontend:** interfaz utilizada por recepcionistas, técnicos y encargados para consultar y registrar información.
2. **Servicios / API:** recibe las solicitudes del frontend y expone las operaciones disponibles del sistema.
3. **Lógica de negocio:** aplica reglas, validaciones, cambios de estado, cálculos y relaciones entre clientes, vehículos y órdenes.
4. **Acceso a datos:** concentra las operaciones de lectura y escritura de información.
5. **Base de datos:** almacena de forma persistente clientes, vehículos, órdenes, diagnósticos, servicios, repuestos y costos.

## Organización frontend / backend

### Frontend

El frontend será responsable de la interacción con el usuario. Incluirá formularios, consultas y vistas para clientes, vehículos, órdenes de trabajo, diagnósticos, repuestos, costos e historial. También realizará validaciones básicas de entrada para mejorar la experiencia de uso, sin sustituir las validaciones obligatorias del backend.

### Backend

El backend será responsable de procesar las solicitudes, aplicar las reglas de negocio, validar la integridad de los datos, calcular costos, controlar el flujo de estados de las órdenes y gestionar el acceso a la base de datos.

### Comunicación

Frontend y backend se comunicarían mediante una **API**, utilizando solicitudes y respuestas estructuradas, por ejemplo mediante HTTP/REST y datos en formato JSON. La interfaz no accedería directamente a la base de datos; toda operación pasaría por los servicios y la lógica de negocio.

## Herramientas utilizadas

- **Git y GitHub:** control de versiones y repositorio.
- **GitHub Issues:** tareas, requisitos, criterios de aceptación y seguimiento.
- **GitHub Projects:** organización del avance mediante tablero Kanban.
- **Visual Paradigm Online:** modelado UML.
- **Markdown:** documentación técnica del repositorio.

## Gestión del proyecto

Se utilizó un enfoque ágil basado en **Kanban**. Para el cierre de la Semana VIII, el tablero utiliza los estados:

`Reserva | Listo | En curso | En revisión | Hecho`

### Estado actual del tablero - 13/10/2026

| Estado | Issues |
|---|---|
| **Hecho** | #1 Diseñar registro de clientes; #7 Definición de arquitectura inicial |
| **Listo** | #2 Diseñar registro de vehículos; #3 Crear módulo de órdenes de trabajo |
| **En curso** | Sin elementos |
| **En revisión** | Sin elementos |
| **Reserva** | #4, #5, #6, #8, #9 y #10 |

Los Issues conservan además el estado que tenían documentado durante la Semana VI, de forma que pueda observarse la evolución del seguimiento sin perder la referencia histórica.

## Estado actual del proyecto

La versión actual corresponde a una **línea base académica 0.1**. El proyecto cuenta con requisitos, historias de usuario, criterios de aceptación, modelos UML, arquitectura por capas, Issues y seguimiento mediante GitHub Projects.

No se presenta como una aplicación terminada. La implementación completa de los módulos, las validaciones y las pruebas funcionales e integración quedan como trabajo de una siguiente etapa.

## Registro breve de cambios y avances

1. Se definieron el problema, objetivo, alcance y usuarios principales del sistema.
2. Se documentaron requisitos funcionales, historias de usuario y criterios de aceptación.
3. Se elaboraron modelos UML para representar funciones, estructura y comportamiento del sistema.
4. Se definió una arquitectura por capas con separación entre frontend, backend, lógica de negocio y persistencia.
5. Se consolidó el seguimiento del proyecto mediante 10 Issues y un tablero Kanban en GitHub Projects.
6. Para el cierre de la Semana VIII se revisaron los Issues, se documentó su estado actual y se sincronizó la documentación del repositorio con el tablero real.

## Issues seleccionados para seguimiento técnico

- **#3 - Crear módulo de órdenes de trabajo:** prioridad alta; estado actual **Listo**. Es el siguiente módulo central preparado para iniciar desarrollo.
- **#6 - Crear historial de servicios:** prioridad media; estado actual **Reserva**. Depende de la persistencia correcta de las órdenes y vehículos.
- **#9 - Implementar validaciones de datos del sistema:** prioridad alta; estado actual **Reserva**. Reduce el riesgo de datos incompletos, duplicados o inválidos.
- **#10 - Realizar pruebas funcionales e integración:** prioridad media; estado actual **Reserva**. Permitirá verificar el funcionamiento individual y conjunto de los módulos.

## Nota técnica de versión

**Versión:** 0.1 - Línea base académica.

**Contenido:** requisitos, historias de usuario, criterios de aceptación, modelos UML, arquitectura por capas, documentación del proyecto, 10 Issues y tablero de seguimiento.

**Cambios controlados:** definición del alcance, consolidación de requisitos, modelado del sistema, decisión arquitectónica, organización del seguimiento técnico y actualización documental de cierre.

**Pendientes:** implementación de los módulos priorizados, validaciones de datos, pruebas funcionales e integración, y fortalecimiento del historial de commits asociado a cada Issue.

**Próximo paso técnico:** pasar el Issue **#3 - Crear módulo de órdenes de trabajo** de **Listo** a **En curso** cuando comience su implementación y relacionar cada cambio de código con su Issue, commit y prueba correspondiente.

## Documentación del repositorio

- [Requisitos](docs/REQUISITOS.md)
- [Modelos UML](docs/UML.md)
- [Arquitectura](docs/ARQUITECTURA.md)
- [Seguimiento del proyecto](docs/SEGUIMIENTO.md)
- [Control de cambios](docs/CONTROL_CAMBIOS.md)
- [Nota técnica de versión 0.1](docs/NOTA_VERSION_0.1.md)

## Enlaces de seguimiento

- GitHub Projects: `https://github.com/users/randolreyes123/projects/1`
- Issues del repositorio: sección **Issues** de este proyecto.
