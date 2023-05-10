class Termostato:
    def __init__(self):
        self.temperaturas = [16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5,
                             24, 24.5, 25]
        self.estado_final = 22
        self.prob_ON = {"16": {"+1": 0.2, "+0.5": 0.5, "+0": 0.3},
                        "16.5-24": {"+1": 0.2, "+0.5": 0.5, "+0": 0.1, "-0.5": 0.2},
                        "24.5": {"+0.5": 0.7, "+0": 0.2, "-0.5": 0.1},
                        "25": {"+0.5": 0, "+0": 0.9, "-0.5": 0.1}}
        self.prob_OFF = {"16": {"+0.5": 0.1, "+0": 0.9},
                         "16.5-24": {"+0.5": 0.1, "+0": 0.4, "-0.5": 0.5},
                         "24.5": {"+0.5": 0.1, "+0": 0.4, "-0.5": 0.5},
                         "25": {"+0": 0.3, "-0.5": 0.7}}

    def proceso1(self):
        valor_estados = {"16": 0, "16.5": 0, "17": 0, "17.5": 0, "18": 0, "18.5": 0, "19": 0,
                         "19.5": 0, "20": 0, "20.5": 0, "21": 0, "21.5": 0, "22": 0,
                         "22.5": 0, "23": 0, "23.5": 0, "24": 0, "24.5": 0, "25": 0}
        ruta = {"16": [], "16.5": [], "17": [], "17.5": [], "18": [], "18.5": [], "19": [],
                         "19.5": [], "20": [], "20.5": [], "21": [], "21.5": [], "22": [],
                         "22.5": [], "23": [], "23.5": [], "24": [], "24.5": [], "25": []}

        costeON = 2
        costeOFF = 1
        valor_estados = self.proceso_optimo(valor_estados, ruta, costeON, costeOFF, 0)
        return valor_estados

    def proceso2(self):
        valor_estados = {"16": 0, "16.5": 0, "17": 0, "17.5": 0, "18": 0, "18.5": 0, "19": 0,
                         "19.5": 0, "20": 0, "20.5": 0, "21": 0, "21.5": 0, "22": 0,
                         "22.5": 0, "23": 0, "23.5": 0, "24": 0, "24.5": 0, "25": 0}
        ruta = {"16": [], "16.5": [], "17": [], "17.5": [], "18": [], "18.5": [], "19": [],
                 "19.5": [], "20": [], "20.5": [], "21": [], "21.5": [], "22": [],
                 "22.5": [], "23": [], "23.5": [], "24": [], "24.5": [], "25": []}
        costeON = 1
        costeOFF = 1
        valor_estados = self.proceso_optimo(valor_estados, ruta, costeON, costeOFF, 0)
        return valor_estados

    def proceso3(self):
        valor_estados = {"16": 0, "16.5": 0, "17": 0, "17.5": 0, "18": 0, "18.5": 0, "19": 0,
                         "19.5": 0, "20": 0, "20.5": 0, "21": 0, "21.5": 0, "22": 0,
                         "22.5": 0, "23": 0, "23.5": 0, "24": 0, "24.5": 0, "25": 0}
        ruta = {"16": [], "16.5": [], "17": [], "17.5": [], "18": [], "18.5": [], "19": [],
                 "19.5": [], "20": [], "20.5": [], "21": [], "21.5": [], "22": [],
                 "22.5": [], "23": [], "23.5": [], "24": [], "24.5": [], "25": []}
        costeON = 1
        costeOFF = 2
        valor_estados = self.proceso_optimo(valor_estados, ruta, costeON, costeOFF, 0)
        return valor_estados

    def proceso4(self):
        valor_estados = {"16": 0, "16.5": 0, "17": 0, "17.5": 0, "18": 0, "18.5": 0, "19": 0,
                         "19.5": 0, "20": 0, "20.5": 0, "21": 0, "21.5": 0, "22": 0,
                         "22.5": 0, "23": 0, "23.5": 0, "24": 0, "24.5": 0, "25": 0}
        ruta = {"16": [], "16.5": [], "17": [], "17.5": [], "18": [], "18.5": [], "19": [],
                "19.5": [], "20": [], "20.5": [], "21": [], "21.5": [], "22": [],
                "22.5": [], "23": [], "23.5": [], "24": [], "24.5": [], "25": []}
        costeON = 3
        costeOFF = 1
        valor_estados = self.proceso_optimo(valor_estados, ruta, costeON, costeOFF, 0)
        return valor_estados

    def proceso5(self):
        valor_estados = {"16": 0, "16.5": 0, "17": 0, "17.5": 0, "18": 0, "18.5": 0, "19": 0,
                         "19.5": 0, "20": 0, "20.5": 0, "21": 0, "21.5": 0, "22": 0,
                         "22.5": 0, "23": 0, "23.5": 0, "24": 0, "24.5": 0, "25": 0}
        ruta = {"16": [], "16.5": [], "17": [], "17.5": [], "18": [], "18.5": [], "19": [],
                "19.5": [], "20": [], "20.5": [], "21": [], "21.5": [], "22": [],
                "22.5": [], "23": [], "23.5": [], "24": [], "24.5": [], "25": []}
        costeON = 1
        costeOFF = 3
        valor_estados = self.proceso_optimo(valor_estados, ruta, costeON, costeOFF, 0)
        return valor_estados

    def proceso_optimo(self, dict_valores, ruta, costeON, costeOFF, num_veces):
        nuevos_valores = []
        for elemento in range(0, len(self.temperaturas)):
            nuevos_valores.append(0)
        contador = 1
        for elemento in self.temperaturas:
            if elemento == 16:
                valor1 = costeON + self.prob_ON["16"]["+1"] * dict_valores["17"] \
                         + self.prob_ON["16"]["+0.5"] * dict_valores["16.5"]\
                         + self.prob_ON["16"]["+0"] * dict_valores["16"]
                valor2 = costeOFF + self.prob_OFF["16"]["+0.5"] * dict_valores["16.5"]\
                         + self.prob_OFF["16"]["+0"] * dict_valores["16"]
                nuevos_valores[0], paso = self.metodo_usado(valor1, valor2)
                ruta["16"].append(paso)

            elif elemento == 22:
                contador += 1
            elif elemento == 24.5:
                nuevos_valores[17] = min(costeON +
                                         self.prob_ON["24.5"]["+0.5"] * dict_valores["25"]
                                         + self.prob_ON["24.5"]["+0"] * dict_valores["24.5"]
                                         + self.prob_ON["24.5"]["-0.5"] * dict_valores["24"],
                                         costeOFF +
                                         self.prob_OFF["24.5"]["+0.5"] * dict_valores["25"]
                                         + self.prob_OFF["24.5"]["+0"] * dict_valores["24.5"]
                                         + self.prob_OFF["24.5"]["-0.5"] * dict_valores["24"])
            elif elemento == 25:
                nuevos_valores[18] = min(costeON +
                                         self.prob_ON["25"]["+0"] * dict_valores["25"]
                                         + self.prob_ON["25"]["-0.5"] * dict_valores["24.5"],
                                         costeOFF +
                                         self.prob_OFF["25"]["+0"] * dict_valores["25"]
                                         + self.prob_OFF["25"]["-0.5"] * dict_valores["24.5"])
            else:
                actual = str(elemento)
                anterior = str(self.temperaturas[contador - 1])
                posterior = str(self.temperaturas[contador + 1])
                next_posterior = str(self.temperaturas[contador + 2])
                nuevos_valores[contador] = min(costeON + self.prob_ON["16.5-24"]["+1"] * dict_valores[next_posterior]
                                               + self.prob_ON["16.5-24"]["+0.5"] * dict_valores[posterior]
                                               + self.prob_ON["16.5-24"]["+0"] * dict_valores[actual]
                                               + self.prob_ON["16.5-24"]["-0.5"] * dict_valores[anterior],
                                               costeOFF + self.prob_OFF["16.5-24"]["+0.5"] * dict_valores[
                                                   posterior]
                                               + self.prob_OFF["16.5-24"]["+0"] * dict_valores[actual]
                                               + self.prob_OFF["16.5-24"]["-0.5"] * dict_valores[
                                                   anterior])
                contador += 1

        fin = self.comparar_valores(nuevos_valores, dict_valores)
        print("En la iteración", num_veces, "tenemos estos datos:")
        contador = 0
        for elemento in self.temperaturas:
            dict_valores[str(elemento)] = round(nuevos_valores[contador], 2)
            print("Valor", elemento, ":", dict_valores[str(elemento)])
            contador += 1
        if not fin:
            num_veces += 1
            dict_valores = self.proceso_optimo(dict_valores, ruta, costeON, costeOFF, num_veces)
        return dict_valores

    def comparar_valores(self, nuevos_valores, valor_estados):
        contador = 0
        for elemento in self.temperaturas:
            num1 = round(nuevos_valores[contador], 2)
            num2 = round(valor_estados[str(round(elemento, 1))], 2)
            if num1 != num2:
                return False
            contador += 1
        return True

    def metodo_usado(self, valorON, valorOFF):
        if valorOFF < valorON:
            return valorOFF, "OFF"
        return valorON, "ON"


prueba = Termostato()
print("Test1")
prueba.proceso1()
print("Test2")
prueba.proceso2()
print("Test3")
prueba.proceso3()
print("Test4")
prueba.proceso4()
print("Test5")
prueba.proceso5()
