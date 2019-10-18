import sys
clave="pepe"
salida="salida"
entrada=(input("Ingresa un nombre: "))
while entrada!=salida and entrada!=clave:
    entrada=(input("Ingresa un nombre: "))
if entrada=="pepe":
    print("Has acertado")
elif entrada=="salir":
    sys.exit()

    