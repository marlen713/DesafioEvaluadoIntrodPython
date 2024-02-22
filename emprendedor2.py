
import math 
# Advertencia al usuario de valores 
print("Ingrese los datos en valores númericos para el buen funcionamiento de éste: ")

# variables de entrada
p = int(input("Digitá el precio de suscripción: ")) 
u_normal = int(input("Coloca el número de Usuarios Normal: ")) 
u_premium = int(input("Coloca el número de Usuarios Premium: ")) 
gt = int(input("Coloca el gasto total: ")) 

# El precio normal 
p_normal = p * u_normal

# Aqui declaro el porcentaje de aumento para los Premium
porcentaje_aumento = 50

# hago la convalidación para sacar el porcentaje
suscripcion_mayor = p * (porcentaje_aumento / 100)

# Aqui saco el precio de los Usuarios
u_premium = p * u_premium + suscripcion_mayor * u_premium

# La formula dada para ver las utilidades
utilidades = p * u_normal + u_premium - gt 

# Esto lo hice para ver por pantalla que me arrojara lo que necesito
# print(utilidades)
# print(suscripcion_mayor)
# print(u_premium)

# entregar output en el formato solicitado
print(f"Los Usuarion Normales pagarán: {math.ceil(p_normal)} pesos y Los Usuarios Premiun deberán de pagar: {math.ceil(u_premium)} pesos, teniendo los Premiun un 50% de recargo. \n El Precio Adicional de cada Suscripción por Usuario Premiun es de: {math.ceil(suscripcion_mayor)}  \n La utilidad del proyecto de entrega de comida para mascotas es de: {math.ceil(utilidades)} pesos")
