'''
Un emprendedor quiere crear una app que provea un servicio de entrega de comida para 
mascotas. Este proyecto tiene buenos pronósticos, pero su éxito dependerá de cuántos 
usuarios pueda alcanzar. La manera en la que se medirá esto es calculando las utilidades del 
proyecto. Estas utilidades se pueden calcular mediante la siguiente fórmula:

Utilidades = P * U - GT
Donde:
P: Precio de Suscripción
U: Número de Usuarios
GT: Gastos Totales

'''
# Advertencia al usuario de valores 
print("Ingrese los datos en valores númericos para el buen funcionamiento de éste: ")

# variables de entrada
p = int(input("Digitá el precio de suscripción: ")) 
u = int(input("Coloca el número de usuario: ")) 
gt = int(input("Coloca el gasto total: ")) 

# Formula dada:
utilidades = p * u - gt

# entregar output en el formato solicitado
print(f"La utilidad del proyecto de entrega de comida para mascotas es de: {utilidades} pesos")

