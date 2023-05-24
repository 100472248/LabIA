from clase_termostato import Termostato

costeON = int(input("Escribe el coste del termostato encendido:"))
costeOFF = int(input("Escribe el coste del termostato apagado:"))
lista_temperaturas = [16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24, 24.5, 25]
termostato = Termostato(costeON, costeOFF)
termostato.ecuacion_Bellman()
print("La tolerancia usada para nuestras pruebas es 0.01")
print("Las iteraciones realizadas hasta la estabilización de los valores esperados son: ", termostato.iteracion)
print("El vector de pesos asociado al MDP es el siguiente:")
print(termostato.valor_estados)
print("El vector de políticas óptimas es el siguiente:")
print(termostato.ruta)