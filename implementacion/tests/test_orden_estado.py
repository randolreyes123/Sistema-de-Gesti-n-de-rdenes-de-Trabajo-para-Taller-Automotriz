import unittest
from orden_estado import Estado, OrdenTrabajo, TransicionInvalida


class PruebasEstado(unittest.TestCase):
    def setUp(self):
        self.orden = OrdenTrabajo("OT-001", "CL-01", "VH-01")

    def test_inicio_recepcion(self):
        self.assertEqual(self.orden.estado, Estado.RECEPCION)

    def test_recepcion_a_diagnostico(self):
        self.orden.avanzar()
        self.assertEqual(self.orden.estado, Estado.DIAGNOSTICO)

    def test_requiere_cliente(self):
        self.orden.cliente_id = ""
        with self.assertRaises(TransicionInvalida): self.orden.avanzar()

    def test_requiere_diagnostico(self):
        self.orden.avanzar()
        with self.assertRaises(TransicionInvalida): self.orden.avanzar()

    def test_requiere_aprobacion(self):
        self.orden.avanzar(); self.orden.diagnostico = "Falla alternador"; self.orden.avanzar()
        with self.assertRaises(TransicionInvalida): self.orden.avanzar()

    def test_requiere_reparacion(self):
        self.orden.avanzar(); self.orden.diagnostico = "Falla alternador"; self.orden.avanzar()
        self.orden.aprobada = True; self.orden.avanzar()
        with self.assertRaises(TransicionInvalida): self.orden.avanzar()

    def test_recorrido_completo(self):
        self.orden.avanzar(); self.orden.diagnostico = "Falla alternador"; self.orden.avanzar()
        self.orden.aprobada = True; self.orden.avanzar()
        self.orden.reparacion_registrada = True; self.orden.avanzar(); self.orden.avanzar()
        self.assertEqual(self.orden.estado, Estado.ENTREGADO)
        self.assertEqual(len(self.orden.historial), 5)

    def test_entregado_es_final(self):
        self.test_recorrido_completo()
        with self.assertRaises(TransicionInvalida): self.orden.avanzar()
        self.assertEqual(self.orden.estado, Estado.ENTREGADO)

    def test_error_no_cambia_estado_ni_historial(self):
        self.orden.avanzar()
        with self.assertRaises(TransicionInvalida): self.orden.avanzar()
        self.assertEqual(self.orden.estado, Estado.DIAGNOSTICO)
        self.assertEqual(len(self.orden.historial), 1)


if __name__ == "__main__": unittest.main()
