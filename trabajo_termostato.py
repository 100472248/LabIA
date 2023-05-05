class algoritmo_IA:
    def __init__(self):
        self.temperaturas = [16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5,
                             24, 24.5, 25]
        self.estado_final = 22
        self.probabilidades_ON = {"16": {"+1": 0.2, "+0.5": 0.5, "+0": 0.3},
                                  "16.5-24": {"+1": 0.2, "+0.5": 0.5, "+0": 0.1, "-0.5": 0.2},
                                  "24.5": {"+0.5": 0.7, "+0": 0.2, "-0.5": 0.1},
                                  "25": {"+0.5": 0, "+0": 0.9, "-0.5": 0.1}}
        self.probabilidades_OFF = {"16": {"+0.5": 0.1, "+0": 0.9},
                                   "16.5-24": {"+0.5": 0.1, "+0": 0.4, "-0.5": 0.5},
                                   "24.5": {"+0.5": 0.1, "+0": 0.4, "-0.5": 0.5},
                                   "25": {"+0": 0.3, "-0.5": 0.7}}

    def proceso1(self):
        valor_cada_estado = {"16": 0, "16.5": 0, "17": 0, "17.5": 0, "18": 0, "18.5": 0, "19": 0,
                             "19.5": 0, "20": 0, "20.5": 0, "21": 0, "21.5": 0, "22": 0,
                             "22.5": 0, "23": 0, "23.5": 0, "24": 0, "24.5": 0, "25": 0}
        costeON = 2
        costeOFF = 1
        valor_cada_estado = self.proceso_optimo(valor_cada_estado, costeON, costeOFF, 0)
        return valor_cada_estado

    def proceso2(self):
        valor_cada_estado = {"16": 0, "16.5": 0, "17": 0, "17.5": 0, "18": 0, "18.5": 0, "19": 0,
                             "19.5": 0, "20": 0, "20.5": 0, "21": 0, "21.5": 0, "22": 0,
                             "22.5": 0, "23": 0, "23.5": 0, "24": 0, "24.5": 0, "25": 0}
        costeON = 1
        costeOFF = 1
        valor_cada_estado = self.proceso_optimo(valor_cada_estado, costeON, costeOFF, 0)
        return valor_cada_estado
    def proceso3(self):
        valor_cada_estado = {"16": 0, "16.5": 0, "17": 0, "17.5": 0, "18": 0, "18.5": 0, "19": 0,
                             "19.5": 0, "20": 0, "20.5": 0, "21": 0, "21.5": 0, "22": 0,
                             "22.5": 0, "23": 0, "23.5": 0, "24": 0, "24.5": 0, "25": 0}
        costeON = 1
        costeOFF = 2
        valor_cada_estado = self.proceso_optimo(valor_cada_estado, costeON, costeOFF, 0)
        return valor_cada_estado

    def proceso_optimo(self, valor_estados, costeON, costeOFF, num_veces):
        if num_veces == 20:
            return valor_estados
        valor_estados["16"] = min(costeON + self.probabilidades_ON["16"]["+1"] * valor_estados["17"]
                                  + self.probabilidades_ON["16"]["+0.5"] * valor_estados["16.5"]
                                  + self.probabilidades_ON["16"]["+0"] * valor_estados["16"],
                                  costeOFF +
                                  self.probabilidades_OFF["16"]["+0.5"] * valor_estados["16.5"]
                                  + self.probabilidades_OFF["16"]["+0"] * valor_estados["16"])
        anterior = 16
        actual = 16.5
        proximo = 17
        proximo_on = 17.5
        for multiplicador in range(0, 16):
            str_actual = str(actual + 0.5 * multiplicador)
            str_anterior = str(anterior + 0.5 * multiplicador)
            str_proximo = str(proximo + 0.5 * multiplicador)
            str_proximo_on = str(proximo_on + 0.5 * multiplicador)
            valor_estados[str_actual] = min(costeON +
                                            self.probabilidades_ON[str_actual]["+1"] * valor_estados[str_proximo_on]
                                            + self.probabilidades_ON[str_actual]["+0.5"] * valor_estados[str_proximo]
                                            + self.probabilidades_ON[str_actual]["+0"] * valor_estados[str_actual]
                                            + self.probabilidades_ON[str_actual]["-0.5"] * valor_estados[str_anterior],
                                            costeOFF + self.probabilidades_OFF[str_actual]["+0.5"] * valor_estados[
                                                str_proximo]
                                            + self.probabilidades_OFF[str_actual]["+0"] * valor_estados[str_actual]
                                            + self.probabilidades_OFF[str_actual]["-0.5"] * valor_estados[str_anterior])

        valor_estados["24.5"] = min(costeON +
                                    self.probabilidades_ON["24.5"]["+0.5"] * valor_estados["25"]
                                    + self.probabilidades_ON["24.5"]["+0"] * valor_estados["24.5"]
                                    + self.probabilidades_ON["24.5"]["-0.5"] * valor_estados["24"],
                                    costeOFF +
                                    self.probabilidades_OFF["24.5"]["+0.5"] * valor_estados["25"]
                                    + self.probabilidades_OFF["24.5"]["+0"] * valor_estados["24.5"]
                                    + self.probabilidades_OFF["24.5"]["-0.5"] * valor_estados["24"])

        valor_estados["25"] = min(costeON +
                                  self.probabilidades_ON["25"]["+0"] * valor_estados["25"]
                                  + self.probabilidades_ON["25"]["-0.5"] * valor_estados["24.5"],
                                  costeOFF +
                                  self.probabilidades_OFF["25"]["+0"] * valor_estados["25"]
                                  + self.probabilidades_OFF["25"]["-0.5"] * valor_estados["24.5"])

        print("En la iteración", num_veces, "tenemos estos datos:")
        for elemento in self.temperaturas:
            print("Valor", elemento, ":", valor_estados[str(elemento)])
        valor_estados = self.proceso_optimo(valor_estados, costeON, costeOFF, num_veces + 1)
        return valor_estados

