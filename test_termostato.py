from unittest import TestCase
from practica_termostato import Termostato
class Test_Algoritmo(TestCase):
    def pesos_correctos(self):
        prueba = Termostato()
        valores1, ruta1, it1 = prueba.proceso1()
        valores2, ruta2, it2 = prueba.proceso2()
        valores3, ruta3, it3 = prueba.proceso3()
        valores4, ruta4, it4 = prueba.proceso4()
        valores5, ruta5, it5 = prueba.proceso5()
        pesosprueba1 = [34.36, 32.26, 29.6, 26.8, 23.96, 21.11, 18.26, 15.4, 12.54, 9.71, 6.76, 4.28, 0, 2.49, 4.98,
                         7.46, 9.91, 12.19, 13.62]
        pesosprueba2 = [17.44, 16.39, 15.06, 13.66, 12.24, 10.82, 9.39, 7.96, 6.53, 5.12, 3.62, 2.47, 0, 2.49, 4.98,
                         7.46, 9.91, 12.19, 13.62]
        pesosprueba3 = [17.97, 16.92, 15.59, 14.19, 12.77, 11.35, 9.92, 8.5, 7.06, 5.66, 4.11, 3.13, 0, 4.99, 9.98,
                        14.96, 19.87, 24.44, 27.3]
        pesosprueba4 = [51.27, 48.12, 44.14, 39.94, 35.68, 31.4, 27.12, 22.84, 18.55, 14.3, 9.89, 6.08, 0, 2.49,
                        4.98, 7.46, 9.91, 12.19, 13.62]
        pesosprueba5 = [18.48, 17.43, 16.1, 14.7, 13.28, 11.86, 10.43, 9.01, 7.57, 6.19, 4.6, 3.8, 0, 7.49,
                        14.98, 22.45, 29.81, 36.66, 40.94]
        contador = 0


