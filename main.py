
class algoritmo_IA:
    def __init__(self):
        pass

    def proceso_principal(self):
        costeON = 1
        costeOFF = 0
        info = {}




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