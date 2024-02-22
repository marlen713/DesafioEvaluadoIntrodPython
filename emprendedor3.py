

# Advertencia al usuario de valores 
print("Ingrese los datos en valores númericos para el buen funcionamiento de éste: ")

# variables de entrada
p = int(input("Digitá el precio de suscripción: ")) 
u = int(input("Coloca el número de usuarios: ")) 
gt = int(input("Coloca el gasto total: ")) 
u_anterior = int(input("Digitá utilidades del Año anterior: ")) 

# Formula dada:
utilidades = p * u - gt

# mostrar la razón entre las utilidades actuales y las del año anterior
razon = utilidades/u_anterior

# entregar output en el formato solicitado
print(f"Las utilidades actuales son: {utilidades}  \n La razon entre las utilidades del año pasado y el año actual es de: {razon:.2f}")