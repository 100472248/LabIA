import csv
import os


class Csv:
    def __init__(self, archivoON: str, archivoOFF: str):
        self.__archivoON = archivoON
        self.__archivoOFF = archivoOFF

    def sacar_datos(self):
        """De aquí se sacan las tablas de las probabilidades como diccionarios de diccionarios."""
        csvfile1 = open(self.__archivoON, 'r', encoding="utf-8")
        csvON = csv.reader(csvfile1)
        csvfile2 = open(self.__archivoOFF, 'r', encoding="utf-8")
        csvOFF = csv.reader(csvfile2)
        matrizON, matrizOFF = [], []
        for fila in csvON:
            matrizON.append(fila)
        for fila in csvOFF:
            matrizOFF.append(fila)
        csvfile1.close()
        csvfile2.close()
        dict_ON, dict_OFF = {}, {}
        temp_base = 16.0
        longitud = 0
        for n in range(len(matrizON)):
            longitud += 1
        for i in range(longitud):
            estado_actual = temp_base + 0.5 * i
            if i % 2 == 0:
                estado_actual = int(estado_actual)
            probOFF, probON = self.organizador_prob(estado_actual, i, matrizOFF, matrizON)
            dict_ON[str(estado_actual)] = probON
            dict_OFF[str(estado_actual)] = probOFF
        return dict_ON, dict_OFF

    def organizador_prob(self, estado_actual, i, matrizOFF, matrizON):
        """Extrae las probabilidades no nulas de las matrices y las organiza en su diccionario correspondiente
        según el estado actual."""
        # probON para meter las del termostato encendido y probOFF las del termostato apagado.
        if estado_actual == 16:
            # Como los datos del csv se sacan en formato str, hay que pasar las probabilidades a float
            probON = {"+0": float(matrizON[0][0]), "+0.5": float(matrizON[0][1]), "+1": float(matrizON[0][2])}
            probOFF = {"+0": float(matrizOFF[0][0]), "+0.5": float(matrizOFF[0][1])}
        elif estado_actual == 22:
            probON = 0
            probOFF = 0
        elif estado_actual == 24.5:
            probON = {"-0.5": float(matrizON[17][16]), "+0": float(matrizON[17][17]),
                      "+0.5": float(matrizON[18][18])}
            probOFF = {"-0.5": float(matrizOFF[17][16]), "+0": float(matrizOFF[17][17]),
                       "+0.5": float(matrizOFF[18][18])}
        elif estado_actual == 25:
            probON = {"-0.5": float(matrizON[18][17]), "+0": float(matrizON[18][18])}
            probOFF = {"-0.5": float(matrizOFF[18][17]), "+0": float(matrizOFF[18][18])}
        else:
            # En este caso, la posición i corresponde a la del estado actual.
            probON = {"-0.5": float(matrizON[i][i - 1]), "+0": float(matrizON[i][i]),
                      "+0.5": float(matrizON[i][i + 1]), "+1": float(matrizON[i][i + 2])}
            probOFF = {"-0.5": float(matrizOFF[i][i - 1]), "+0": float(matrizOFF[i][i]),
                       "+0.5": float(matrizOFF[i][i + 1])}
        return probOFF, probON
