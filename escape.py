# La velocidad de escape se calcula mediante la siguiente fórmula: Ve = √2gr

# Importamos math
import math

# Advertencia al usuario de valores 
print("Ingrese los datos en valores númericos para el buen funcionamiento de éste: ")

# variables de entrada
r = float(input("Ingrese el radio en Kilometros: "))
g = float(input("Ingrese la constante g: "))


# El Radio lo multiplico por 1000, ya que 1Km es 1000 Metro
r = 6371 * 1000

# La constante fija es 9.8

# La función Math.sqrt() retorna la raíz cuadrada de un número
ve = math.sqrt(2*g*r)

# entregar output en el formato solicitado
print(f"La velocidad de Escape es de {ve:.1f}[m/s]")



