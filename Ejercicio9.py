import sys
clave="pepe"
salida="salida"
entrada=(input("Ingresa un nombre: "))
while entrada!=salida and entrada!=clave:
    entrada=(input("Ingresa un nombre: "))
if entrada==clave:
    print("Has acertado")
elif entrada==salida:
    sys.exit()