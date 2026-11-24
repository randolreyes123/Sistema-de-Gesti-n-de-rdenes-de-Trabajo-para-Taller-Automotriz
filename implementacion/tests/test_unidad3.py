import unittest
from orden_estado import *

class Calidad(unittest.TestCase):
    def orden(self):
        return OrdenTrabajo('OT-001','CL-01','VH-01')
    def rechazar(self, orden, estado):
        anterior = orden.historial.copy()
        try:
            with self.assertRaises(TransicionInvalida):
                ESTADOS[estado].siguiente(orden)
            with self.assertRaises(TransicionInvalida):
                orden.avanzar()
        finally:
            self.assertEqual(orden.estado, estado)
            self.assertEqual(orden.historial, anterior)
    def test_cp01_recepcion(self):
        for campo in ('numero','cliente_id','vehiculo_id'):
            for valor in ('',' ',None,123):
                with self.subTest(campo=campo,valor=valor):
                    o=self.orden(); setattr(o,campo,valor)
                    self.rechazar(o,Estado.RECEPCION)
        o=self.orden(); self.assertEqual(Recepcion().siguiente(o),Estado.DIAGNOSTICO)
        o.avanzar(); self.assertEqual(o.estado,Estado.DIAGNOSTICO)
    def test_cp02_diagnostico(self):
        for valor in ('',' ',None,123):
            with self.subTest(valor=valor):
                o=self.orden(); o.avanzar(); o.diagnostico=valor
                self.rechazar(o,Estado.DIAGNOSTICO)
        o=self.orden(); o.avanzar(); o.diagnostico='Alternador'
        self.assertEqual(Diagnostico().siguiente(o),Estado.ESPERANDO_APROBACION)
        o.avanzar(); self.assertEqual(o.estado,Estado.ESPERANDO_APROBACION)
    def espera(self):
        o=self.orden(); o.avanzar(); o.diagnostico='Alternador'; o.avanzar(); return o
    def test_cp03_aprobacion(self):
        for valor in (False,None,'False',1):
            with self.subTest(valor=valor):
                o=self.espera(); o.aprobada=valor; self.rechazar(o,Estado.ESPERANDO_APROBACION)
        o=self.espera(); o.aprobada=True
        self.assertEqual(EsperandoAprobacion().siguiente(o),Estado.EN_REPARACION)
        o.avanzar(); self.assertEqual(o.estado,Estado.EN_REPARACION)
    def reparacion(self):
        o=self.espera(); o.aprobada=True; o.avanzar(); return o
    def test_cp04_reparacion(self):
        for valor in (False,None,'False',1):
            with self.subTest(valor=valor):
                o=self.reparacion(); o.reparacion_registrada=valor; self.rechazar(o,Estado.EN_REPARACION)
        o=self.reparacion(); o.reparacion_registrada=True
        self.assertEqual(EnReparacion().siguiente(o),Estado.TERMINADO)
        o.avanzar(); self.assertEqual(o.estado,Estado.TERMINADO)
    def test_cp05_entrega(self):
        o=self.reparacion(); o.reparacion_registrada=True; o.avanzar(); o.avanzar()
        self.assertEqual(o.estado,Estado.ENTREGADO)
        estados=list(Estado)
        self.assertEqual(o.historial,[f'{a.value} -> {b.value}' for a,b in zip(estados,estados[1:])])
        self.rechazar(o,Estado.ENTREGADO)
        self.assertEqual(self.orden().historial,[])
