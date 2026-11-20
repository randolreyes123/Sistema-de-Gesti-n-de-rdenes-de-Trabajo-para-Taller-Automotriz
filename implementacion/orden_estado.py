"""Prototipo aislado del patrón State para RF-03 (sin base de datos ni API)."""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum


class Estado(str, Enum):
    RECEPCION = "Recepción"
    DIAGNOSTICO = "Diagnóstico"
    ESPERANDO_APROBACION = "Esperando aprobación"
    EN_REPARACION = "En reparación"
    TERMINADO = "Terminado"
    ENTREGADO = "Entregado"


class TransicionInvalida(ValueError):
    pass


@dataclass
class OrdenTrabajo:
    numero: str
    cliente_id: str
    vehiculo_id: str
    estado: Estado = Estado.RECEPCION
    diagnostico: str = ""
    aprobada: bool = False
    reparacion_registrada: bool = False
    historial: list[str] = field(default_factory=list)

    def avanzar(self) -> None:
        siguiente = ESTADOS[self.estado].siguiente(self)
        self.historial.append(f"{self.estado.value} -> {siguiente.value}")
        self.estado = siguiente


class EstadoOrden:
    """Interfaz del comportamiento cambiante por estado."""
    def siguiente(self, orden: OrdenTrabajo) -> Estado:
        raise NotImplementedError


class Recepcion(EstadoOrden):
    def siguiente(self, orden):
        if not all((orden.numero.strip(), orden.cliente_id.strip(), orden.vehiculo_id.strip())):
            raise TransicionInvalida("La orden requiere número, cliente y vehículo")
        return Estado.DIAGNOSTICO


class Diagnostico(EstadoOrden):
    def siguiente(self, orden):
        if not orden.diagnostico.strip():
            raise TransicionInvalida("Debe registrar el diagnóstico")
        return Estado.ESPERANDO_APROBACION


class EsperandoAprobacion(EstadoOrden):
    def siguiente(self, orden):
        if not orden.aprobada:
            raise TransicionInvalida("Falta aprobación del trabajo")
        return Estado.EN_REPARACION


class EnReparacion(EstadoOrden):
    def siguiente(self, orden):
        if not orden.reparacion_registrada:
            raise TransicionInvalida("Debe registrar la reparación")
        return Estado.TERMINADO


class Terminado(EstadoOrden):
    def siguiente(self, orden):
        return Estado.ENTREGADO


class Entregado(EstadoOrden):
    def siguiente(self, orden):
        raise TransicionInvalida("Una orden entregada no puede avanzar")


ESTADOS: dict[Estado, EstadoOrden] = {
    Estado.RECEPCION: Recepcion(),
    Estado.DIAGNOSTICO: Diagnostico(),
    Estado.ESPERANDO_APROBACION: EsperandoAprobacion(),
    Estado.EN_REPARACION: EnReparacion(),
    Estado.TERMINADO: Terminado(),
    Estado.ENTREGADO: Entregado(),
}
