from clase_termostato import Termostato
temperatura = input("Escribe un número del 16 al 25:")
if "." in temperatura:
    temperatura = float(temperatura)
else:
    temperatura = int(temperatura)

costeON = int(input("Escribe el coste del termostato encendido:"))
costeOFF = int(input("Escribe el coste del termostato apagado:"))
print("Para temperatura", temperatura, ", coste encendido", costeON, "y coste apagado", costeOFF,
      "; tenemos los siguientes resultados:")
prueba = Termostato(temperatura, costeON, costeOFF)
peso, ruta, num_iteraciones = prueba.proceso_optimo()
print("->Num_iteraciones:", num_iteraciones)
print("->Peso total:", peso)
print("->Ruta realizada:", ruta)
