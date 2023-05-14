import random
from unittest import TestCase
from clase_termostato import Termostato
class Test_Algoritmo(TestCase):
    """Trata de comprobar el funcionamiento correcto del programa y sus excepciones."""

    def test_Bellman_correcto(self):
        """Se estudia si Bellman funciona para cada temperatura con costes válidos al azar."""
        temperaturas = [16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5,
                        24, 24.5, 25]
        temperatura = random.choice(temperaturas)
        costeON = random.randint(1, 10)
        costeOFF = random.randint(1, 10)
        prueba = Termostato(temperatura, costeON, costeOFF)
        prueba.ecuacion_Bellman()
        pesos, rutas, iteraciones = prueba.valor_estados, prueba.ruta, prueba.iteracion
        for estado in temperaturas:
            prueba = Termostato(estado, costeON, costeOFF)
            peso_estado, ruta_estado, iteracion_estado = prueba.proceso_optimo()
            self.assertEqual(pesos[str(estado)], peso_estado)
            self.assertEqual(rutas[str(estado)], ruta_estado)

    def test_temperatura_incorrecta(self):
        """Prueba si salta error con una tempearuta no perteneciente al grupo de estados (15 ºC)."""
        costeON = random.randint(1, 10)
        costeOFF = random.randint(1, 10)
        with self.assertRaises(ValueError) as excepcion:
            Termostato(15, costeON, costeOFF)
        self.assertEqual(excepcion.exception.__str__(), "Temperatura no perteneciente al conjunto de estados.")

    def test_coste_encendido_negativo(self):
        """Prueba si salta una excepción si se indica un costeON negativo."""
        temperaturas = [16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5,
                        24, 24.5, 25]
        temperatura = random.choice(temperaturas)
        costeOFF = random.randint(1, 10)
        with self.assertRaises(ValueError) as excepcion:
            Termostato(temperatura, -1, costeOFF)
        self.assertEqual(excepcion.exception.__str__(), "El coste de encendido debe ser positivo.")

    def test_coste_apagado_negativo(self):
        """Prueba si salta una excepción si se indica un costeOFF negativo."""
        temperaturas = [16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5,
                        24, 24.5, 25]
        temperatura = random.choice(temperaturas)
        costeON = random.randint(1, 10)
        with self.assertRaises(ValueError) as excepcion:
            Termostato(temperatura, costeON, -1)
        self.assertEqual(excepcion.exception.__str__(), "El coste de apagado debe ser positivo.")

    def test_coste_encendido_nulo(self):
        """Prueba si salta error al indicar un costeON nulo."""
        temperaturas = [16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5,
                        24, 24.5, 25]
        temperatura = random.choice(temperaturas)
        costeOFF = random.randint(1, 10)
        with self.assertRaises(ValueError) as excepcion:
            Termostato(temperatura, 0, costeOFF)
        self.assertEqual(excepcion.exception.__str__(), "El coste de encendido debe ser positivo.")

    def test_coste_apagado_nulo(self):
        """Prueba si salta error al indicar un costeOFF nulo."""
        temperaturas = [16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5,
                        24, 24.5, 25]
        temperatura = random.choice(temperaturas)
        costeON = random.randint(1, 10)
        with self.assertRaises(ValueError) as excepcion:
            Termostato(temperatura, costeON, 0)
        self.assertEqual(excepcion.exception.__str__(), "El coste de apagado debe ser positivo.")
