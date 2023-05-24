import random
from unittest import TestCase
from clase_termostato import Termostato

class Test_algoritmo(TestCase):
    """Trata de comprobar el funcionamiento correcto del programa y sus excepciones."""

    def test_coste_encendido_negativo(self):
        """Prueba si salta una excepción si se indica un costeON negativo."""
        costeOFF = random.randint(1, 10)
        with self.assertRaises(ValueError) as excepcion:
            Termostato(-1, costeOFF)
        self.assertEqual(excepcion.exception.__str__(), "El coste de encendido debe ser positivo.")

    def test_coste_apagado_negativo(self):
        """Prueba si salta una excepción si se indica un costeOFF negativo."""
        costeON = random.randint(1, 10)
        with self.assertRaises(ValueError) as excepcion:
            Termostato(costeON, -1)
        self.assertEqual(excepcion.exception.__str__(), "El coste de apagado debe ser positivo.")

    def test_coste_encendido_nulo(self):
        """Prueba si salta error al indicar un costeON nulo."""
        costeOFF = random.randint(1, 10)
        with self.assertRaises(ValueError) as excepcion:
            Termostato(0, costeOFF)
        self.assertEqual(excepcion.exception.__str__(), "El coste de encendido debe ser positivo.")

    def test_coste_apagado_nulo(self):
        """Prueba si salta error al indicar un costeOFF nulo."""
        costeON = random.randint(1, 10)
        with self.assertRaises(ValueError) as excepcion:
            Termostato(costeON, 0)
        self.assertEqual(excepcion.exception.__str__(), "El coste de apagado debe ser positivo.")
