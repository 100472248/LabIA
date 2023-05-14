from Csv import Csv


class Termostato:
    def __init__(self, temp_inicial: float, costeON: int, costeOFF: int):
        # Indicamos las distintas temperaturas y sus probabilidades.
        self.temperaturas = [16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5,
                             24, 24.5, 25]
        # Los costes y la temperatura inicial se chequean.
        self.__temp_inicial, self.__costeON, self.__costeOFF = self.check_valores(temp_inicial,
                                                                                  costeON, costeOFF)
        self.iteracion = 0
        # De estos archivos csv se sacan los diccionarios de probabilidades (uno para ON y otro para OFF).
        self.lector = Csv("probON.csv", "probOFF.csv")
        self.prob_ON, self.prob_OFF = self.lector.sacar_datos()

        self.valor_estados = {"16": 0, "16.5": 0, "17": 0, "17.5": 0, "18": 0, "18.5": 0, "19": 0,
                              "19.5": 0, "20": 0, "20.5": 0, "21": 0, "21.5": 0, "22": 0,
                              "22.5": 0, "23": 0, "23.5": 0, "24": 0, "24.5": 0, "25": 0}

        self.ruta = {"16": [], "16.5": [], "17": [], "17.5": [], "18": [], "18.5": [], "19": [],
                     "19.5": [], "20": [], "20.5": [], "21": [], "21.5": [], "22": [],
                     "22.5": [], "23": [], "23.5": [], "24": [], "24.5": [], "25": []}

    def proceso_optimo(self):
        """Devuelve el peso, ruta y el num_iteraciones del estado elegido como inicial"""
        self.ecuacion_Bellman()
        peso_temperatura = self.valor_estados[str(self.__temp_inicial)]
        ruta_temperatura = self.ruta[str(self.__temp_inicial)]
        return peso_temperatura, ruta_temperatura, self.iteracion

    def ecuacion_Bellman(self):
        """Realiza la ecuación de Bellman según los costes elegidos para todos los estados."""
        nuevos_valores = []
        contador = 1
        for elemento in self.temperaturas:
            # Diferenciamos los estados 16, 22, 24.5 y 25 porque no siguen la misma estructura
            # que el resto.
            if elemento == 16:
                valorON = self.__costeON + self.prob_ON["16"]["+1"] * self.valor_estados["17"] \
                          + self.prob_ON["16"]["+0.5"] * self.valor_estados["16.5"] \
                          + self.prob_ON["16"]["+0"] * self.valor_estados["16"]
                valorOFF = self.__costeOFF + self.prob_OFF["16"]["+0.5"] * self.valor_estados["16.5"] \
                           + self.prob_OFF["16"]["+0"] * self.valor_estados["16"]
                next_valor, paso = self.metodo_usado(valorON, valorOFF)
                self.ruta["16"].append(paso)
                nuevos_valores.append(next_valor)

            elif elemento == 22:
                # Como es el estado final, su coste siempre es 0.
                nuevos_valores.append(0)
                contador += 1
            elif elemento == 24.5:
                valorON = self.__costeON + self.prob_ON["24.5"]["+0.5"] * self.valor_estados["25"] \
                          + self.prob_ON["24.5"]["+0"] * self.valor_estados["24.5"] \
                          + self.prob_ON["24.5"]["-0.5"] * self.valor_estados["24"]
                valorOFF = self.__costeOFF + self.prob_OFF["24.5"]["+0.5"] * self.valor_estados["25"] \
                           + self.prob_OFF["24.5"]["+0"] * self.valor_estados["24.5"] \
                           + self.prob_OFF["24.5"]["-0.5"] * self.valor_estados["24"]
                next_valor, paso = self.metodo_usado(valorON, valorOFF)
                self.ruta["24.5"].append(paso)
                nuevos_valores.append(next_valor)

            elif elemento == 25:
                valorON = self.__costeON + self.prob_ON["25"]["+0"] * self.valor_estados["25"] \
                          + self.prob_ON["25"]["-0.5"] * self.valor_estados["24.5"]
                valorOFF = self.__costeOFF + self.prob_OFF["25"]["+0"] * self.valor_estados["25"] \
                           + self.prob_OFF["25"]["-0.5"] * self.valor_estados["24.5"]
                next_valor, paso = self.metodo_usado(valorON, valorOFF)
                self.ruta["25"].append(paso)
                nuevos_valores.append(next_valor)
            else:
                # Se calcula el estado anterior en la lista y los dos siguientes porque son los que
                # están conectados con el actual.
                actual = str(elemento)
                # Utilizamos la lista de temperaturas para que no hay problema entre flotantes y enteros.
                anterior = str(self.temperaturas[contador - 1])
                posterior = str(self.temperaturas[contador + 1])
                next_posterior = str(self.temperaturas[contador + 2])
                # Ecuación de Bellman. En vez de usar min(), hemos optado en crear una función metodo_usado
                # que devuelev el valor menor y la opción escogida (ON o OFF).
                valorON = self.__costeON + self.prob_ON[actual]["+1"] * self.valor_estados[next_posterior] \
                          + self.prob_ON[actual]["+0.5"] * self.valor_estados[posterior] \
                          + self.prob_ON[actual]["+0"] * self.valor_estados[actual] \
                          + self.prob_ON[actual]["-0.5"] * self.valor_estados[anterior]
                valorOFF = self.__costeOFF + self.prob_OFF[actual]["+0.5"] * self.valor_estados[posterior] \
                           + self.prob_OFF[actual]["+0"] * self.valor_estados[actual] \
                           + self.prob_OFF[actual]["-0.5"] * self.valor_estados[anterior]
                next_valor, paso = self.metodo_usado(valorON, valorOFF)
                # Se añade la elección a la ruta
                self.ruta[actual].append(paso)
                nuevos_valores.append(next_valor)
                contador += 1
        # En comparar_valores, analizamos si los nuevos valores son idénticos o no a los anteriores.
        fin = self.comparar_valores(nuevos_valores)
        contador = 0
        # Se actualizan los pesos
        for elemento in self.temperaturas:
            self.valor_estados[str(elemento)] = round(nuevos_valores[contador], 2)
            contador += 1
        # Si no es el fin, se repite de forma recursiva el proceso.
        if not fin:
            self.iteracion += 1
            self.ecuacion_Bellman()

    def check_valores(self, temperatura, costeON, costeOFF):
        """Función para checkear """
        if temperatura not in self.temperaturas:
            raise ValueError("Temperatura no perteneciente al conjunto de estados.")
        if costeON < 1:
            raise ValueError("El coste de encendido debe ser positivo.")
        if costeOFF < 1:
            raise ValueError("El coste de apagado debe ser positivo.")
        return temperatura, costeON, costeOFF

    def comparar_valores(self, nuevos_valores):
        """Para ver si se repite o no el proceso"""
        contador = 0
        for elemento in self.temperaturas:
            num1 = round(nuevos_valores[contador], 2)
            num2 = round(self.valor_estados[str(round(elemento, 1))], 2)
            if num1 != num2:
                return False
            contador += 1
        return True

    @staticmethod
    def metodo_usado(valorON, valorOFF):
        """Para devolver si el termostato está ON o OFF"""
        if valorOFF < valorON:
            return valorOFF, "OFF"
        return valorON, "ON"
