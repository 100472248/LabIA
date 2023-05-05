
class algoritmo_IA:
    def __init__(self):
        self.temperaturas = [16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5,
                             24, 24.5, 25]
        self.estado_final = 22
        self.probabilidades_ON = {"16":{"+1": 0.2, "+0.5": 0.5, "+0": 0.3},
                                  "16.5-24":{"+1": 0.2, "+0.5": 0.5, "+0": 0.1, "-0.5":0.2},
                                  "24.5":{"+0.5": 0.7, "+0": 0.2, "-0.5":0.1},
                                  "25":{"+0.5": 0, "+0": 0.9, "-0.5":0.1}}
        self.probabilidades_OFF = {"16":{"+0.5": 0.1, "+0": 0.9},
                                  "16.5-24":{"+0.5": 0.1, "+0": 0.4, "-0.5":0.5},
                                  "24.5":{"+0.5": 0.1, "+0": 0.4, "-0.5":0.5},
                                  "25":{"+0": 0.3, "-0.5":0.7}}

    def proceso1(self):
        valor_cada_estado = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        costeON = 2
        costeOFF = 1
        info = {}

    def proceso2(self):
        valor_cada_estado = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        costeON = 1
        costeOFF = 1
        info = {}

    def proceso3(self):
        valor_cada_estado = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        costeON = 1
        costeOFF = 2
        info = {}

    def proceso_optimo(self, estado_actual, info, costeON, costeOFF):
        if estado_actual == 22:
            return x




def pol_opt(estado: float, i: int):
    if i == 0:
        return 0
    if estado == 16:
        return min(12 + 0.5 * pol_opt(16.5, i - 1) + 0.2 * pol_opt(17, i - 1) + 0.3 * pol_opt(16, i - 1),
                   0.9 * pol_opt(16, i - 1) + 0.1 * pol_opt(16.5, i - 1))
    elif estado == 22:
        return 0
    elif estado == 24.5:
        return min(12 + 0.1 * pol_opt(24, i - 1) + 0.7 * pol_opt(25, i - 1) + 0.2 * pol_opt(24.5, i - 1),
                   0.1 * pol_opt(25, i - 1) + 0.4 * pol_opt(24.5, i - 1) + 0.5 * pol_opt(24, i - 1))
    elif estado == 25:
        return min(12 + 0.9 * pol_opt(25, i - 1) + 0.1 * pol_opt(24.5, i - 1),
                   0.3 * pol_opt(25, i - 1) + 0.7 * pol_opt(24.5, i - 1))
    else:
        return min(
            12 + 0.1 * pol_opt(estado - 0.5, i - 1) + 0.2 * pol_opt(estado, i - 1) + 0.5 * pol_opt(estado + 0.5, i - 1)
            + 0.2 * pol_opt(estado + 1, i - 1), 0.5 * pol_opt(estado - 0.5, i - 1) + 0.4 * pol_opt(estado, i - 1) +
            0.1 * pol_opt(estado + 0.5, i - 1))
